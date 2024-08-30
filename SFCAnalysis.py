"""
To begin, let's import all of our dependencies, including our data and python packages
"""
import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc as pm
import pytensor
import matplotlib.pyplot as plt
import pdb
from mpl_toolkits.mplot3d import Axes3D
import json
import pickle # python3
import seaborn as sns
import scipy.io as sio
import numpyro

import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc as pm
import pytensor
import matplotlib.pyplot as plt
import pdb
from mpl_toolkits.mplot3d import Axes3D
import json
import pickle # python3
import seaborn as sns
import scipy.io as sio
import numpyro
import pymc.sampling.jax as pmjax
if __name__ == '__main__':                                            #This statement is to allow for parallel sampling in windows. Linux distributions don't require this.
    print(f"Running on PyMC3 v{pm.__version__}")
    color = '#87ceeb'
    az.style.use("arviz-darkgrid")

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

    df = pd.read_pickle('SFC.pkl')
    df = addLabelsToDF(df)
    #df = df.loc[df.NPulses==10]
    EPP = df.EnergyPerPulse.values
    EPP = [float(i) for i in EPP]
    EPP = np.array(EPP)
    EPP[EPP<=0] = 0
    freqs = sio.loadmat('SFCFreqs.mat')
    freqs = freqs['freqs']
    freqs = np.squeeze(freqs)
    freqsWhere = np.where(freqs<=200)
    freqsWhere = freqsWhere[0]
    nRows = len(df)
    thetaCoh = np.nan*np.ones((nRows,))
    alphaCoh = np.nan*np.ones((nRows,))
    betaCoh = np.nan*np.ones((nRows,))
    lgCoh = np.nan*np.ones((nRows,))
    hgCoh = np.nan*np.ones((nRows,))
    freqVec = np.nan*np.ones((nRows,))
    labels = df.labels.values
    for ck in range(nRows):
        curSFC = df.meanSFC[ck]
        curSFC = curSFC[freqsWhere]
        thetaCoh[ck] = curSFC[1]
        alphaCoh[ck] = curSFC[2]
        betaCoh[ck] = np.max(curSFC[3:6])
        #betaCoh[ck] = np.max(curSFC[3])
        lgCoh[ck] = np.max(curSFC[6:14])
        #lgCoh[ck] = np.max(curSFC[6])
        hgCoh[ck] = np.max(curSFC[14:34])
        #hgCoh[ck] = np.max(curSFC[14])
        maxSFC = np.nanmax(curSFC)

        freqLoc = np.where(curSFC==maxSFC)
        freqVec[ck] = freqsWhere[freqLoc]

    df['thetaCoh'] = thetaCoh
    df['alphaCoh'] = alphaCoh
    df['betaCoh'] = betaCoh
    df['lgCoh'] = lgCoh
    df['hgCoh'] = hgCoh
    df['freqVec'] = freqVec
    df['lepp'] = np.log(EPP+0.01)
    df['lISI'] = np.log(df.ISI+0.01)
    data = df
    """
    Convert power to energy based on laser power levels and pulse widths, then save this into the dataframe
    """
    #Xenergy = data.Energy.values
    #lenData = len(Xenergy)
    #XenergyPerPulse = np.zeros((lenData,))
    #XPW = data.Pulse_Width.values
    #for ck in range(lenData):

        #XenergyPerPulse[ck] = Xenergy[ck]/XPW[ck]
        #if XenergyPerPulse[ck] < 0:
            #XenergyPerPulse[ck] = 0
    data['XenergyPerPulse'] = EPP

    XenergyPerPulse = data.XenergyPerPulse
    #Grab response variable
    #MaxZ = data["Max_BARS_Z"].astype(aesara.config.floatX)               #Convert to tensor
    #MaxZ = np.log(MaxZ+0.1)
    #Plot distribution of data (log scale)
    #sns.distplot(MaxZ, kde=True)


    """
    Now let's setup some meta data for our model analyses. We will set the number of burn in samples, which "primes" the markov chain Monte Carlo (MCMC) algorithm, and number of
    samples to draw from the posterior. In general, less "well behaved" data will require more samples to get MCMC to converge to steady state.
    """
    numBurnIn = 400
    numSamples = 500
    RANDOM_SEED = 7
    
    """
    Finally get our independent variables, ISI and energy per pulse
    """
    #np.log(data['XenergyPerPulse']+0.1)
    #XenergyPerPulse = np.asarray(np.log(XenergyPerPulse+0.01))
    # Plot data vs predictors
    #fig = plt.figure()
    #ax = fig.add_subplot(projection='3d')
    #ax.scatter(XenergyPerPulse,XDist,data['Max_Z_Score'])
    #plt.xlabel('Energy')
    #plt.ylabel('ISI')
    
    data = data.loc[data.lepp>=-4]
    data.reset_index(drop=True, inplace = True)
    lepp = data.lepp
    theta = data.lgCoh.values
    XDist = data.ISI.values
    XDist = np.log(XDist+0.01)
    plt.scatter(data.lepp,theta)
    plt.show()
    """
    Since we are doing a within-subjects repeated measures design, we need to create a mapping between subjects and data. Each animal had a 16 channel recording array in A1 that
    is recording from different groups of neurons. So we sort by animal and electrode
    """
    data.animal_code = data.DataID
    animal_codes = np.unique(data.animal_code)
    animal_codes_map = np.arange(0,len(animal_codes))
    newCodes = np.zeros((len(data.animal_code)),dtype=int)
    for ck in range(len(data.animal_code)):
        curCode = data.animal_code[ck]
        newCode = np.where(curCode == animal_codes)
        newCode = newCode[0][0]
        newCodes[ck] = int(newCode)
    data['animal_code'] = newCodes
    animal_code_idx = data['animal_code'].values#data.animal_code.values
    n_channels = len(data.animal_code.unique())
    #theta = (theta-np.mean(theta))/(np.std(theta))
    #sns.distplot(theta)
    #plt.show()
    """
    Now define the model
    """
    prMean = np.nanmean(theta)
    with pm.Model() as Heirarchical_Regression:
        # Hyperpriors for group nodes
        mu_a = pm.Normal("mu_a", mu=prMean, sigma=0.1)
        sigma_a = pm.HalfNormal("sigma_a", 0.1)
        mu_b = pm.Normal("mu_b", mu=prMean, sigma=0.1)
        sigma_b = pm.HalfNormal("sigma_b", 0.1)
        mu_b2 = pm.Normal("mu_b2",mu=prMean, sigma=0.1)
        sigma_b2 = pm.HalfNormal("sigma_b2",0.1)
        mu_b3 = pm.Normal("mu_b3", 1)
        sigma_b3 = pm.HalfNormal("sigma_b3",0.1)

        sigma_nu = pm.Exponential("sigma_nu",5.0)
        #sigma_kurt = pm.Exponential("sigma_kurt",5.0)
        #Base layer
        nu = pm.HalfCauchy('nu', sigma_nu)          #Nu for robust regression
        #kurt = pm.HalfCauchy('kurt',sigma_kurt)
        a_offset = pm.Normal('a_offset', mu=prMean, sigma=0.1, shape=(n_channels))
        a = pm.Deterministic("a", mu_a + a_offset * sigma_a)

        b1_offset = pm.Normal('b1_offset', mu=prMean, sigma=0.1, shape=(n_channels))
        b1 = pm.Deterministic("b1", mu_b + b1_offset * sigma_b)

        b2_offset = pm.Normal("b2_offset",mu=prMean, sigma=0.1, shape=(n_channels))
        b2 = pm.Deterministic("b2", mu_b2 + b2_offset*sigma_b2)

        b3_offset = pm.Normal("b3_offset",mu=prMean, sigma=0.1, shape=(n_channels))
        b3 = pm.Deterministic("b3", mu_b3 + b3_offset*sigma_b3)

        eps = pm.HalfCauchy("eps", 5,shape=(n_channels))

        regression = pm.Deterministic('regression',a[animal_code_idx] + (b1[animal_code_idx] * lepp) + (b2[animal_code_idx] * XDist) +(b3[animal_code_idx]*lepp*XDist))

        likelihood = pm.StudentT("MaxZ_like",nu=nu,mu=regression,sigma=eps[animal_code_idx], observed= theta)
    with Heirarchical_Regression:
        if __name__ == '__main__':
                step = pm.NUTS()
                rTrace = pmjax.sample_numpyro_nuts(numSamples, tune=numBurnIn, target_accept=0.95,chains = 2)
    """
    Now do model analytics
    """
    intercept = rTrace.posterior["a"]                #Grab the posterior distribution of a
    EnergySlope = rTrace.posterior["b1"]                    #Grab the posterior distribution of b1
    ISISlope = rTrace.posterior["b2"]                    #Grab the posterior distribution of B
    InteractionSlope = rTrace.posterior["b3"]                    #Grab the posterior distribution of B
    err = rTrace.posterior["eps"]                    #Grab the posterior distribution of model error
    f_dict = {'size':16}

    fig, ([ax1, ax2, ax3], [ax4, ax5, ax6]) = plt.subplots(2,3, figsize=(12,6))
    for ax, estimate, title, xlabel in zip(fig.axes,
                                [intercept, EnergySlope, ISISlope,InteractionSlope, err],
                                ['Intercept', 'Energy Slope','ISI Slope','Interaction Slope','Error Parameter'],
                                [r'$a$', r'$\beta1$', r'$\beta 2$', r'$\beta 3$' , r'$err$']):
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

    az.plot_trace(rTrace, var_names=["mu_a", "mu_b", "mu_b2", "mu_b3", "sigma_a", "sigma_b","sigma_b2","sigma_b3", "eps"])

    az.plot_trace(rTrace, var_names=["a"])

    az.plot_trace(rTrace, var_names=["b1"])

    az.plot_trace(rTrace, var_names=["b2"])

    az.plot_trace(rTrace, var_names=["b3"])

    az.plot_trace(rTrace, var_names=["nu"])
    plt.show()
    pdb.set_trace()
    az.to_netcdf(rTrace,filename='HierModel_HGTrace.netcdf')
    az.to_netcdf(ppc,filename='HierModel_HGPPC.netcdf')