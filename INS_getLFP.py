#--------------------------------------------------------------------------------------------------------------------------------------------
# Authors: Brandon S Coventry            Wisconsin Institute for Translational Neuroengineering
# Date: 02/03/2023                       The night it was so cold, my car battery died at work... Wisconsin is cold
# Purpose: This is the header file for SPyke, a Python toolbox for analyzing Neural Spiking Data.
# Interface: At the moment, this uses TDT based reading and analysis, but can be extended to other systems.
# Revision History: Will be tracked in Github.
# Notes: N/A
#--------------------------------------------------------------------------------------------------------------------------------------------
# Imports go here. Global use imports will be put here, we will upload specifics as needed.
import numpy as np
import tdt              #For reading in tdt files
import matplotlib.pyplot as plt
import dask
from SPyke import Spike_Processed
import pdb
if __name__ == "__main__":
    dataStore = {}
    animalName = 'INS2102'
    Date = '20210216'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'C://DataRepos//INS//INS2102//20210216//5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore
    pdb.set_trace()
    #filterData = SpikeClass.filterData(Type)
    #SpikeClass.stimArtifactRemoval(algo='Template')

