#--------------------------------------------------------------------------------------------------------------------------------------------
# Authors: Brandon S Coventry            Wisconsin Institute for Translational Neuroengineering
# Date: 04/22/2024                       Wisconsin is springlike? Finally?
# Purpose: This performs dirichlet regression for wave decomposition
# Revision History: Will be tracked in Github.
# Notes: N/A
#--------------------------------------------------------------------------------------------------------------------------------------------
# Imports go here. Global use imports will be put here, we will upload specifics as needed.
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
import matlab.engine
import jax

numSamples = 5000
numBurnIn = 2000

def wavePreProcess(wave):
    waveVec = np.zeros((8,))
    [nSamps,nCols] = np.shape(wave)
    waveHold = np.zeros((nSamps,))
    for ck in range(nSamps):
        waveHold[ck] = float(wave[ck][0])*0.01
    waveVec[0:7] = waveHold[0:7]
    #Take care of non-wave components to ensure all sums to 1.
    waveVec[7] = np.sum(waveHold[7:nSamps])
    return waveVec

if __name__ == '__main__': 
    #Define the model
    df = pd.read_pickle('LFPVelocity.pkl')
    N = df.shape[0]
    epp = df['EnergyPerPulse'].values
    prct = df['prctSVD']
    PCAdims = 8
    x_expt_cond = np.zeros((N,PCAdims))
    for ck in range(len(epp)):
        curEpp = epp[ck]*np.ones((PCAdims,))
        x_expt_cond[ck,:] = curEpp

    waveDecomp = np.zeros((N,PCAdims))
    for ck in range(N):
        curWave = prct[ck]
        waveDecomp[ck,:] = wavePreProcess(curWave)
    WP = [f"wp-{i}" for i in range(PCAdims)]
    REPS = [f"{epp}-{i}" for i in range(N)]
    coords = {"wp": WP, "energy": REPS}
    intercept = np.ones_like((N,))        #Intercept the size of number of datapoints, N.
    
    with pm.Model(coords=coords) as dirichlet_reg:
        b0 = pm.Normal("a", 0, 5, dims=("wp",))
        b1 = pm.Normal("b", 0, 2.5, dims=("wp",))
        eta = pm.Deterministic("eta",b0[None, :] * intercept + b1[None, :] * x_expt_cond, dims=("energy", "wp"))
        mu = pm.Deterministic("mu", pm.math.exp(eta), dims=("energy", "wp"))
        y = pm.Dirichlet("y", mu, observed=waveDecomp, dims=("energy", "wp"))
    with dirichlet_reg:
        step = pm.NUTS()
        rTrace = pm.sample(numSamples, tune=numBurnIn, target_accept=0.90,chains = 4)
    
    az.summary(rTrace, var_names=["b0", "b1"], hdi_prob=0.95)
    pdb.set_trace()