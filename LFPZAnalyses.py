#----------------------------------------------------------------------------------------------------------------------------------
# Author: Brandon S Coventry PhD
# Date: 03/18/24
# Purpose: COG Analyses
# Revision History: See github
#----------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pdb
import arviz as az
import pymc as pm
import aesara
import matplotlib.pyplot as plt
import pdb
from mpl_toolkits.mplot3d import Axes3D
import json
import pickle # python3
import seaborn as sns

import jax
if __name__ == '__main__': 
    print(f"Running on PyMC v{pm.__version__}")
    LFPZ = pd.read_pickle('LFPZ.pkl')
    def RMS(data):
        return np.sqrt(np.mean(data**2))
    epp = LFPZ.EnergyPerPulse.values
    epp = [float(ele) for ele in epp]
    epp = np.array(epp)
    epp[epp<0] = 0
    lepp = np.log(epp+0.001)
    ISI = LFPZ.ISI.values
    nISI = np.log(ISI+0.001)
    z = LFPZ.ZMax.values
    mLFP = LFPZ.meanLFP.values
    maxZArray = np.zeros((len(epp),))
    RMSArray = np.zeros((len(epp),))
    for ck in range(len(epp)):
        curMLFP = mLFP[ck]
        curZ = z[ck]
        maxZArray[ck] = np.max(curZ)
        RMSArray[ck] = RMS(curMLFP)
    
    #Create a distribution plot of the data.
    sns.scatterplot(x=np.log(epp+0.01), y=RMSArray)
    plt.show()
    sns.scatterplot(x=np.log(epp+0.01), y=maxZArray)
    plt.show()
    #Lets organize data for hierarchy
    animalID = np.zeros((len(epp),),dtype=int)
    IDXList = {}
    countIDX = 0
    for ck in range(len(epp)):
        IDX = LFPZ.DataID[ck].split('//')
        curIDX = IDX[0]
        elec = LFPZ.Electrode[ck]
        keyIDX = curIDX+str(elec)
        if keyIDX in IDXList.keys():
            animalID[ck] = int(IDXList[keyIDX])
        else:
            animalID[ck] = int(countIDX)
            IDXList[keyIDX] = int(countIDX)
            countIDX = countIDX+1
    
    numSamples = 5000
    numBurnIn = 2000
    n_channels = len(np.unique(animalID))
    
    with pm.Model() as Heirarchical_Regression:
        # Hyperpriors for group nodes
        mu_a = pm.Normal("mu_a", mu=0.0, sigma=5)
        sigma_a = pm.HalfNormal("sigma_a", 5)
        mu_b = pm.Normal("mu_b", mu=0.0, sigma=5)
        sigma_b = pm.HalfNormal("sigma_b", 5)
        mu_b2 = pm.Normal("mu_b2",mu=0.0, sigma=5)
        sigma_b2 = pm.HalfNormal("sigma_b2",5)
        mu_b3 = pm.Normal("mu_b3", 5)
        sigma_b3 = pm.HalfNormal("sigma_b3",5)
        
        sigma_nu = pm.Exponential("sigma_nu",5.0)
        #Base layer
        nu = pm.HalfCauchy('nu', sigma_nu)          #Nu for robust regression
        a_offset = pm.Normal('a_offset', mu=0, sigma=5, shape=(n_channels))
        a = pm.Deterministic("a", mu_a + a_offset * sigma_a)

        b1_offset = pm.Normal('b1_offset', mu=0, sigma=5, shape=(n_channels))
        b1 = pm.Deterministic("b1", mu_b + b1_offset * sigma_b)
        
        b2_offset = pm.Normal("b2_offset",mu=0, sigma=5, shape=(n_channels))
        b2 = pm.Deterministic("b2", mu_b2 + b2_offset*sigma_b2)

        b3_offset = pm.Normal("b3_offset",mu=0, sigma=5, shape=(n_channels))
        b3 = pm.Deterministic("b3", mu_b3 + b3_offset*sigma_b3)

        eps = pm.HalfCauchy("eps", 5,shape=(n_channels))

        regression = a[animalID] + (b1[animalID] * lepp) + (b2[animalID] * nISI) +(b3[animalID]*lepp*nISI)

        likelihood = pm.StudentT("MaxZ_like",nu=nu,mu=regression,sigma=eps[animalID], observed= RMSArray) 

    """
    Now we run the model!
    """
    with Heirarchical_Regression:
        if __name__ == '__main__':
                step = pm.NUTS()
                rTrace = pm.sample(numSamples, tune=numBurnIn, target_accept=0.90,chains = 4, nuts_sampler="nutpie")
                #rTrace = pm.sampling_jax.sample_numpyro_nuts(numSamples, tune=numBurnIn, target_accept=0.95,chains = 4)
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
    pdb.set_trace()



