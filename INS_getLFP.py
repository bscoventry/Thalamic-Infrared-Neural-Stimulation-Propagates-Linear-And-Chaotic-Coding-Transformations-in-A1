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
    dataPath = 'C://DataRepos//INS//INS2102//20210216//5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    SpikeClass = Spike_Processed(dataPath,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    pdb.set_trace()
    #filterData = SpikeClass.filterData(Type)
    #SpikeClass.stimArtifactRemoval(algo='Template')

