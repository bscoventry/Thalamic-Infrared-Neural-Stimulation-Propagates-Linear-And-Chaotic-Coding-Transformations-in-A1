import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytensor
pytensor.config.floatX = "float32"
import pymc as pm
import matplotlib.pyplot as plt
import pdb
from mpl_toolkits.mplot3d import Axes3D
import json
import pickle # python3
import seaborn as sns
import scipy.io as sio
import numpyro
import pymc.sampling.jax as pmjax
import pdb

if __name__ == '__main__':                                            #This statement is to allow for parallel sampling in windows. Linux distributions don't require this.
    numSamples = 5000
    numBurnIn = 2000
    RANDOM_SEED = 77
    print(f"Running on PyMC3 v{pm.__version__}")
    color = '#87ceeb'
    az.style.use("arviz-darkgrid")

    #Load data
    """
    Here we will load data in, and do necessary extraction. For the moment, we are interested in purely excitatory responses on pulse trains
    """
    def addLabelsToDF(df):
        EPP = df.EnergyPerPulse.values

        nRows = len(EPP)
        labels = np.zeros((nRows,),dtype=int)
        for ck in range(nRows):

            if float(EPP[ck]) <0.5:
                labels[ck] = 0
            elif 0.5<= float(EPP[ck]) < 1:
                labels[ck] = 1
            elif 1<= float(EPP[ck]) < 1.5:
                labels[ck] = 2
            elif 1.5<= float(EPP[ck]) < 2:
                labels[ck] = 3
            elif 2<= float(EPP[ck]) < 2.5:
                labels[ck] = 4
            elif 2.5<= float(EPP[ck]) < 3:
                labels[ck] = 5
            elif 3<= float(EPP[ck]) < 3.5:
                labels[ck] = 6
            elif float(EPP[ck])>=3.5:
                labels[ck] = 7
        df['labels'] = labels
        return df

    df = pd.read_pickle('SpikeN1P2.pkl')
    df = addLabelsToDF(df)
    #df = df.loc[df.NPulses==10]
    EPP = df.EnergyPerPulse.values
    EPP = [float(i) for i in EPP]
    EPP = np.array(EPP)
    EPP[EPP<=0] = 0
    # Now, sort data into singlular arrays
    [nrows,ncols] = np.shape(df)
    spikeList = []
    N1P2List = []
    ePP = df.EnergyPerPulse.values
    ePP = [float(i) for i in ePP]
    ePP = np.array(ePP)
    ePPidx = np.where(ePP<0)
    ePPidx = ePPidx[0]
    ePP[ePPidx] = 0
    ePPList = []
    ISIList = []
    
    for ck in range(nrows):

        curSPK = df.spkRate[ck]
        spkMean = np.mean(curSPK)
        if spkMean >5:
            spikeList.append(spkMean)
            curLFP = df.N1P2[ck]
            N1P2Mean = np.mean(curLFP)*1000000
            N1P2List.append(N1P2Mean)
            #ePPList.append(ePP[ck])
            ISIList.append(float(df.ISI[ck]))
    spikeList = np.log(np.array(spikeList))
    ISIList = np.array(ISIList)
    #ISIList = np.log(ISIList)
    plt.scatter(spikeList,N1P2List)
    
    
    pdb.set_trace()
    #ePPList = np.array(ePPList)
    #lepp = np.log(ePPList+0.001)
    eMean = np.nanmean(ISIList)
    N1P2List = np.array(N1P2List)
    prMean = np.nanmean(N1P2List)
    with pm.Model() as Heirarchical_Regression:
        # Hyperpriors for group nodes

        #Base layer
        nu = pm.HalfCauchy('nu', 5)          #Nu for robust regression
        #kurt = pm.HalfCauchy('kurt',sigma_kurt)
        a = pm.Normal('a', mu=prMean, sigma=0.1)
        #a = pm.Deterministic("a", mu_a + a_offset * sigma_a)

        b1 = pm.Normal('b1', mu=prMean, sigma=0.1)
        #b1 = pm.Deterministic("b1", mu_b + b1_offset * sigma_b)

        b2 = pm.Normal("b2",mu=prMean, sigma=0.1)
        #b2 = pm.Deterministic("b2", mu_b2 + b2_offset*sigma_b2)

        eps = pm.HalfCauchy("eps", 5)

        regression = pm.Deterministic('regression',a + (b1 * spikeList) + (b2 * ISIList))

        likelihood = pm.StudentT("MaxZ_like",nu=nu,mu=regression,sigma=eps, observed= N1P2List)
    with Heirarchical_Regression:
        if __name__ == '__main__':
                step = pm.NUTS()
                rTrace = pm.sample(numSamples, tune=numBurnIn, target_accept=0.90,chains = 2,nuts_sampler="nutpie")
    """
    Now do model analytics
    """
    intercept = rTrace.posterior["a"]                #Grab the posterior distribution of a
    SpikeSlope = rTrace.posterior["b1"]                    #Grab the posterior distribution of b1
    ISISlope = rTrace.posterior["b2"]                    #Grab the posterior distribution of B
    #InteractionSlope = rTrace.posterior["b3"]                    #Grab the posterior distribution of B
    err = rTrace.posterior["eps"]                    #Grab the posterior distribution of model error
    f_dict = {'size':16}

    fig, ([ax1, ax2, ax3], [ax4, ax5, ax6]) = plt.subplots(2,3, figsize=(12,6))
    for ax, estimate, title, xlabel in zip(fig.axes,
                                [intercept, EnergySlope, ISISlope, err],
                                ['Intercept', 'Energy Slope','ISI Slope','Error Parameter'],
                                [r'$a$', r'$\beta1$', r'$\beta 2$', r'$err$']):
        pm.plot_posterior(estimate, point_estimate='mode', ax=ax, color=color,hdi_prob=0.95)
        ax.set_title(title, fontdict=f_dict)
        ax.set_xlabel(xlabel, fontdict=f_dict)

    """
    Let's check out model with posterior predictive checks
    """
    with Heirarchical_Regression:
        if __name__ == '__main__':
            ppc = pm.sample_posterior_predictive(rTrace, random_seed=RANDOM_SEED)

    az.plot_bpv(ppc, hdi_prob=0.95,kind='p_value')
    az.plot_ppc(ppc)

    """
    Now let's plot our trace diagnostics
    """

    #pm.model_to_graphviz(Heirarchical_Regression)

    #az.plot_trace(rTrace, var_names=["mu_a", "mu_b", "mu_b2", "mu_b3", "sigma_a", "sigma_b","sigma_b2","sigma_b3", "eps"])

    az.plot_trace(rTrace, var_names=["a"])

    az.plot_trace(rTrace, var_names=["b1"])

    az.plot_trace(rTrace, var_names=["b2"])

    az.plot_trace(rTrace, var_names=["nu"])
    plt.show()
    pdb.set_trace()
    az.to_netcdf(rTrace,filename='HierModel_HGTrace.netcdf')
    az.to_netcdf(ppc,filename='HierModel_HGPPC.netcdf')
    pdb.set_trace()