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
from scipy.integrate import simpson
import jax
from sklearn.linear_model import LinearRegression
import scipy.io as sio
from scipy.signal import sosfiltfilt
if __name__ == '__main__': 
    randomSeed = 777
    color = '#87ceeb'
    az.style.use("arviz-darkgrid")
    print(f"Running on PyMC v{pm.__version__}")
    LFPZ = pd.read_pickle('LFPZ.pkl')
    def calcZ(data):
        m = np.mean(data[0:305])
        s = np.std(data[0:305])
        Z = (data-m)/s
        return Z
    def RMS(data):
        return np.sqrt(np.mean(data**2))
    def intAUC(data):
        return simpson(data)
    def parsePW(data):
        
        str1 = data.find("PW")
        str2 = data.find("PU")
        totStr = data[str2:str1+1]
        SplitSTR = totStr.split("_")
        if len(SplitSTR) == 2:
            val = SplitSTR[1]
            val = float(val[0:val.find("P")])
        elif len(SplitSTR) == 3:
            val = SplitSTR[2]
            if val == '1P':
                val = 0.1
            elif val == '2P':
                val = 0.2
            elif val == '3P':
                val = 0.3
            elif val == '4P':
                val = 0.4
            elif val == '5P':
                val = 0.5
            elif val == '6P':
                val = 0.6
            elif val == '7P':
                val = 0.7
            elif val == '8P':
                val = 0.8
            elif val == '9P':
                val = 0.9
            else:
                print('Error in conversion')
        else:
            print(data + ' Error')
        return val
    
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
    RMSArray = []
    AUC = []
    slopeArray = []
    slopeScore = []
    dataID = []
    electrodes = []
    counter = 0
    eVec = []
    ISIVec = []
    N1P2Peak = []
    SOS10 = sio.loadmat('SOS10')
    SOS10 = np.ascontiguousarray(SOS10['SOS'])
    for ck in range(len(epp)):
        PW = parsePW(LFPZ.DataID[ck])
        curMLFP = mLFP[ck]
        
        curMLFP = sosfiltfilt(SOS10,curMLFP)
        stimWin = (LFPZ.NPulses[ck]*PW)+((LFPZ.NPulses[ck]-1)*LFPZ.ISI[ck])
        win = int(np.ceil(1526*(stimWin*0.001)))+77            #Add 50ms for offset responses
        
        ZStim = calcZ(curMLFP)
        Zwhere = np.where(np.abs(ZStim)>2)
        Zwhere = Zwhere[0]
        
        if len(Zwhere)>= 1:
            #This is above threshold
            #curMLFP = mLFP[ck]
            stimLFP = curMLFP[305:305+win+153]               #Stimulus window plus 100ms
            N1 = np.where(stimLFP==np.min(stimLFP))
            N1Win = curMLFP[305+N1[0][0]:-1]
            P2 = np.where(N1Win==np.max(N1Win))
            
            YReg = curMLFP[305+N1[0][0]:305+P2[0][0]+N1[0][0]]
            XReg = np.arange(0,len(YReg))
            try:
                reg = LinearRegression().fit(XReg.reshape(-1,1), YReg)
                slopeArray.append(reg.coef_[0])
                slopeScore.append(reg.score(XReg.reshape(-1,1), YReg))
            except:
                pdb.set_trace()
            P2 = P2[0][0]+N1[0][0]
            N1Peak = curMLFP[305+N1[0][0]]
            P2Peak = curMLFP[305+P2]
            N1P2Peak.append(np.abs(N1Peak)+np.abs(P2Peak))
            P2 = P2+77              #Plus 50 milliseconds
            integralArray = curMLFP[305:305+P2]
            AUC.append(simpson(np.abs(integralArray)))
            RMSArray.append(RMS(integralArray))
            dataID.append(LFPZ.DataID[ck])
            electrodes.append(LFPZ.Electrode[ck])
            eVec.append(epp[ck])
            ISIVec.append(ISI[ck]) 
            counter = counter + 1
            
    eVec = np.asarray(eVec)
    slopeArray = np.asarray(slopeArray)
    ISIVec= np.asarray(ISIVec)
    epp = eVec
    lepp = np.log(epp+0.0001)
    nISI = np.log(ISIVec+0.001)
    AUC = np.log(np.asarray(AUC)+0.0001)
    RMSArray = np.log(np.asarray(RMSArray))
    N1P2Peak = np.asarray(N1P2Peak)
    #pdb.set_trace()
    sns.scatterplot(x=np.log(epp+0.01), y=RMSArray)
    plt.show()
    
    #slopeArray=np.log(slopeArray+0.000001)
    #Lets organize data for hierarchy
    animalID = np.zeros((len(epp),),dtype=int)
    IDXList = {}
    countIDX = 0
    for ck in range(len(epp)):
        
        IDX = dataID[ck].split('//')
        curIDX = IDX[0]
        elec = electrodes[ck]
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
        mu_a = pm.Normal("mu_a", mu=0.0, sigma=1)
        sigma_a = pm.HalfNormal("sigma_a", 1)
        mu_b = pm.Normal("mu_b", mu=0.0, sigma=1)
        sigma_b = pm.HalfNormal("sigma_b", 1)
        mu_b2 = pm.Normal("mu_b2",mu=0.0, sigma=1)
        sigma_b2 = pm.HalfNormal("sigma_b2",1)
        mu_b3 = pm.Normal("mu_b3", mu=0.0,sigma=1)
        sigma_b3 = pm.HalfNormal("sigma_b3",1)
        
        sigma_nu = pm.Exponential("sigma_nu",5.0)
        #Base layer
        nu = pm.HalfCauchy('nu', sigma_nu)          #Nu for robust regression
        a_offset = pm.Normal('a_offset', mu=0, sigma=1, shape=(n_channels))
        a = pm.Deterministic("a", mu_a + a_offset * sigma_a)

        b1_offset = pm.Normal('b1_offset', mu=0, sigma=1, shape=(n_channels))
        b1 = pm.Deterministic("b1", mu_b + b1_offset * sigma_b)
        
        b2_offset = pm.Normal("b2_offset",mu=0, sigma=1, shape=(n_channels))
        b2 = pm.Deterministic("b2", mu_b2 + b2_offset*sigma_b2)

        b3_offset = pm.Normal("b3_offset",mu=0, sigma=1, shape=(n_channels))
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
    plt.show()
    with Heirarchical_Regression:
        pm.compute_log_likelihood(rTrace)
    
    with Heirarchical_Regression:
        if __name__ == '__main__':
            ppc = pm.sample_posterior_predictive(rTrace, random_seed=randomSeed)

    az.plot_bpv(ppc, hdi_prob=0.95,kind='p_value')
    az.plot_ppc(ppc)
    pdb.set_trace()
    #az.to_netcdf(rTrace,'N1P2_RMS_Prior1_HyperPrior1_nonlogRMS.netcdf')

    #Comment this section out if no model comps want to be run
    # with pm.Model() as Heirarchical_Regression:
    #     # Hyperpriors for group nodes
    #     mu_a = pm.Normal("mu_a", mu=0.0, sigma=5)
    #     sigma_a = pm.HalfNormal("sigma_a", 5)
    #     mu_b = pm.Normal("mu_b", mu=0.0, sigma=5)
    #     sigma_b = pm.HalfNormal("sigma_b", 5)
    #     mu_b2 = pm.Normal("mu_b2",mu=0.0, sigma=5)
    #     sigma_b2 = pm.HalfNormal("sigma_b2",5)
    #     mu_b3 = pm.Normal("mu_b3", mu=0.0,sigma=5)
    #     sigma_b3 = pm.HalfNormal("sigma_b3",5)
        
    #     sigma_nu = pm.Exponential("sigma_nu",5.0)
    #     #Base layer
    #     nu = pm.HalfCauchy('nu', sigma_nu)          #Nu for robust regression
    #     a_offset = pm.Normal('a_offset', mu=0, sigma=5, shape=(n_channels))
    #     a = pm.Deterministic("a", mu_a + a_offset * sigma_a)

    #     b1_offset = pm.Normal('b1_offset', mu=0, sigma=5, shape=(n_channels))
    #     b1 = pm.Deterministic("b1", mu_b + b1_offset * sigma_b)
        
    #     b2_offset = pm.Normal("b2_offset",mu=0, sigma=5, shape=(n_channels))
    #     b2 = pm.Deterministic("b2", mu_b2 + b2_offset*sigma_b2)

    #     b3_offset = pm.Normal("b3_offset",mu=0, sigma=5, shape=(n_channels))
    #     b3 = pm.Deterministic("b3", mu_b3 + b3_offset*sigma_b3)

    #     eps = pm.HalfCauchy("eps", 5,shape=(n_channels))

    #     regression = a[animalID] + (b1[animalID] * lepp) + (b2[animalID] * nISI) +(b3[animalID]*lepp*nISI)

    #     likelihood = pm.StudentT("MaxZ_like",nu=nu,mu=regression,sigma=eps[animalID], observed= RMSArray) 

    # """
    # Now we run the model!
    # """
    # with Heirarchical_Regression:
    #     if __name__ == '__main__':
    #             step = pm.NUTS()
    #             rTrace = pm.sample(numSamples, tune=numBurnIn, target_accept=0.90,chains = 4, nuts_sampler="nutpie")
    #             #rTrace = pm.sampling_jax.sample_numpyro_nuts(numSamples, tune=numBurnIn, target_accept=0.95,chains = 4)
    # """
    # Now do model analytics
    # """
    # intercept = rTrace.posterior["a"]                #Grab the posterior distribution of a
    # EnergySlope = rTrace.posterior["b1"]                    #Grab the posterior distribution of b1
    # ISISlope = rTrace.posterior["b2"]                    #Grab the posterior distribution of B
    # InteractionSlope = rTrace.posterior["b3"]                    #Grab the posterior distribution of B
    # err = rTrace.posterior["eps"]                    #Grab the posterior distribution of model error
    # f_dict = {'size':16}
    
    # fig, ([ax1, ax2, ax3], [ax4, ax5, ax6]) = plt.subplots(2,3, figsize=(12,6))
    # for ax, estimate, title, xlabel in zip(fig.axes,
    #                             [intercept, EnergySlope, ISISlope,InteractionSlope, err],
    #                             ['Intercept', 'Energy Slope','ISI Slope','Interaction Slope','Error Parameter'],
    #                             [r'$a$', r'$\beta1$', r'$\beta 2$', r'$\beta 3$' , r'$err$']):
    #     pm.plot_posterior(estimate, point_estimate='mode', ax=ax, color=color,hdi_prob=0.95)
    #     ax.set_title(title, fontdict=f_dict)
    #     ax.set_xlabel(xlabel, fontdict=f_dict)
    # plt.show()
    # with Heirarchical_Regression:
    #     pm.compute_log_likelihood(rTrace)
    
    # with Heirarchical_Regression:
    #     if __name__ == '__main__':
    #         ppc = pm.sample_posterior_predictive(rTrace, random_seed=randomSeed)

    # az.plot_bpv(ppc, hdi_prob=0.95,kind='p_value')
    # az.plot_ppc(ppc)
    # pdb.set_trace()
    # az.to_netcdf(rTrace,'N1P2_RMS_Prior5_HyperPrior5.netcdf')

    # with pm.Model() as Heirarchical_Regression:
    #     # Hyperpriors for group nodes
    #     mu_a = pm.Normal("mu_a", mu=0.0, sigma=0.5)
    #     sigma_a = pm.HalfNormal("sigma_a", 0.5)
    #     mu_b = pm.Normal("mu_b", mu=0.0, sigma=0.5)
    #     sigma_b = pm.HalfNormal("sigma_b", 0.5)
    #     mu_b2 = pm.Normal("mu_b2",mu=0.0, sigma=0.5)
    #     sigma_b2 = pm.HalfNormal("sigma_b2",0.5)
    #     mu_b3 = pm.Normal("mu_b3", mu=0.0,sigma=0.5)
    #     sigma_b3 = pm.HalfNormal("sigma_b3",0.5)
        
    #     sigma_nu = pm.Exponential("sigma_nu",5.0)
    #     #Base layer
    #     nu = pm.HalfCauchy('nu', sigma_nu)          #Nu for robust regression
    #     a_offset = pm.Normal('a_offset', mu=0, sigma=0.5, shape=(n_channels))
    #     a = pm.Deterministic("a", mu_a + a_offset * sigma_a)

    #     b1_offset = pm.Normal('b1_offset', mu=0, sigma=0.5, shape=(n_channels))
    #     b1 = pm.Deterministic("b1", mu_b + b1_offset * sigma_b)
        
    #     b2_offset = pm.Normal("b2_offset",mu=0, sigma=0.5, shape=(n_channels))
    #     b2 = pm.Deterministic("b2", mu_b2 + b2_offset*sigma_b2)

    #     b3_offset = pm.Normal("b3_offset",mu=0, sigma=0.5, shape=(n_channels))
    #     b3 = pm.Deterministic("b3", mu_b3 + b3_offset*sigma_b3)

    #     eps = pm.HalfCauchy("eps", 5,shape=(n_channels))

    #     regression = a[animalID] + (b1[animalID] * lepp) + (b2[animalID] * nISI) +(b3[animalID]*lepp*nISI)

    #     likelihood = pm.StudentT("MaxZ_like",nu=nu,mu=regression,sigma=eps[animalID], observed= RMSArray) 

    # """
    # Now we run the model!
    # """
    # with Heirarchical_Regression:
    #     if __name__ == '__main__':
    #             step = pm.NUTS()
    #             rTrace = pm.sample(numSamples, tune=numBurnIn, target_accept=0.90,chains = 4, nuts_sampler="nutpie")
    #             #rTrace = pm.sampling_jax.sample_numpyro_nuts(numSamples, tune=numBurnIn, target_accept=0.95,chains = 4)
    # """
    # Now do model analytics
    # """
    # intercept = rTrace.posterior["a"]                #Grab the posterior distribution of a
    # EnergySlope = rTrace.posterior["b1"]                    #Grab the posterior distribution of b1
    # ISISlope = rTrace.posterior["b2"]                    #Grab the posterior distribution of B
    # InteractionSlope = rTrace.posterior["b3"]                    #Grab the posterior distribution of B
    # err = rTrace.posterior["eps"]                    #Grab the posterior distribution of model error
    # f_dict = {'size':16}
    
    # fig, ([ax1, ax2, ax3], [ax4, ax5, ax6]) = plt.subplots(2,3, figsize=(12,6))
    # for ax, estimate, title, xlabel in zip(fig.axes,
    #                             [intercept, EnergySlope, ISISlope,InteractionSlope, err],
    #                             ['Intercept', 'Energy Slope','ISI Slope','Interaction Slope','Error Parameter'],
    #                             [r'$a$', r'$\beta1$', r'$\beta 2$', r'$\beta 3$' , r'$err$']):
    #     pm.plot_posterior(estimate, point_estimate='mode', ax=ax, color=color,hdi_prob=0.95)
    #     ax.set_title(title, fontdict=f_dict)
    #     ax.set_xlabel(xlabel, fontdict=f_dict)
    # plt.show()
    # with Heirarchical_Regression:
    #     pm.compute_log_likelihood(rTrace)
    
    # with Heirarchical_Regression:
    #     if __name__ == '__main__':
    #         ppc = pm.sample_posterior_predictive(rTrace, random_seed=randomSeed)

    # az.plot_bpv(ppc, hdi_prob=0.95,kind='p_value')
    # az.plot_ppc(ppc)
    # pdb.set_trace()
    # az.to_netcdf(rTrace,'N1P2_RMS_Prior0_5_HyperPrior0_5.netcdf')

    # with pm.Model() as Heirarchical_Regression:
    #     # Hyperpriors for group nodes
    #     mu_a = pm.Normal("mu_a", mu=0.0, sigma=10)
    #     sigma_a = pm.HalfNormal("sigma_a", 10)
    #     mu_b = pm.Normal("mu_b", mu=0.0, sigma=10)
    #     sigma_b = pm.HalfNormal("sigma_b", 10)
    #     mu_b2 = pm.Normal("mu_b2",mu=0.0, sigma=10)
    #     sigma_b2 = pm.HalfNormal("sigma_b2",10)
    #     mu_b3 = pm.Normal("mu_b3", mu=0.0,sigma=10)
    #     sigma_b3 = pm.HalfNormal("sigma_b3",10)
        
    #     sigma_nu = pm.Exponential("sigma_nu",5.0)
    #     #Base layer
    #     nu = pm.HalfCauchy('nu', sigma_nu)          #Nu for robust regression
    #     a_offset = pm.Normal('a_offset', mu=0, sigma=10, shape=(n_channels))
    #     a = pm.Deterministic("a", mu_a + a_offset * sigma_a)

    #     b1_offset = pm.Normal('b1_offset', mu=0, sigma=10, shape=(n_channels))
    #     b1 = pm.Deterministic("b1", mu_b + b1_offset * sigma_b)
        
    #     b2_offset = pm.Normal("b2_offset",mu=0, sigma=10, shape=(n_channels))
    #     b2 = pm.Deterministic("b2", mu_b2 + b2_offset*sigma_b2)

    #     b3_offset = pm.Normal("b3_offset",mu=0, sigma=10, shape=(n_channels))
    #     b3 = pm.Deterministic("b3", mu_b3 + b3_offset*sigma_b3)

    #     eps = pm.HalfCauchy("eps", 5,shape=(n_channels))

    #     regression = a[animalID] + (b1[animalID] * lepp) + (b2[animalID] * nISI) +(b3[animalID]*lepp*nISI)

    #     likelihood = pm.StudentT("MaxZ_like",nu=nu,mu=regression,sigma=eps[animalID], observed= RMSArray) 

    # """
    # Now we run the model!
    # """
    # with Heirarchical_Regression:
    #     if __name__ == '__main__':
    #             step = pm.NUTS()
    #             rTrace = pm.sample(numSamples, tune=numBurnIn, target_accept=0.90,chains = 4, nuts_sampler="nutpie")
    #             #rTrace = pm.sampling_jax.sample_numpyro_nuts(numSamples, tune=numBurnIn, target_accept=0.95,chains = 4)
    # """
    # Now do model analytics
    # """
    # intercept = rTrace.posterior["a"]                #Grab the posterior distribution of a
    # EnergySlope = rTrace.posterior["b1"]                    #Grab the posterior distribution of b1
    # ISISlope = rTrace.posterior["b2"]                    #Grab the posterior distribution of B
    # InteractionSlope = rTrace.posterior["b3"]                    #Grab the posterior distribution of B
    # err = rTrace.posterior["eps"]                    #Grab the posterior distribution of model error
    # f_dict = {'size':16}
    
    # fig, ([ax1, ax2, ax3], [ax4, ax5, ax6]) = plt.subplots(2,3, figsize=(12,6))
    # for ax, estimate, title, xlabel in zip(fig.axes,
    #                             [intercept, EnergySlope, ISISlope,InteractionSlope, err],
    #                             ['Intercept', 'Energy Slope','ISI Slope','Interaction Slope','Error Parameter'],
    #                             [r'$a$', r'$\beta1$', r'$\beta 2$', r'$\beta 3$' , r'$err$']):
    #     pm.plot_posterior(estimate, point_estimate='mode', ax=ax, color=color,hdi_prob=0.95)
    #     ax.set_title(title, fontdict=f_dict)
    #     ax.set_xlabel(xlabel, fontdict=f_dict)
    # plt.show()
    # with Heirarchical_Regression:
    #     pm.compute_log_likelihood(rTrace)
    
    # with Heirarchical_Regression:
    #     if __name__ == '__main__':
    #         ppc = pm.sample_posterior_predictive(rTrace, random_seed=randomSeed)

    # az.plot_bpv(ppc, hdi_prob=0.95,kind='p_value')
    # az.plot_ppc(ppc)
    # pdb.set_trace()
    # az.to_netcdf(rTrace,'N1P2_RMS_Prior10_HyperPrior10.netcdf')




            