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
from SPyke import Spike
import pdb
dataPath = 'L://Ludwig Lab//Data//Rat//ViantRodent//P121//P121-230609-115622' #'C://Users//coventry//Desktop//P119-230317-165356'
stores = None             #Load all stores
streamStore = 'streams'
rawDataStore = 'TDT2'
debug = 0
stim = 0
SpikeClass = Spike(dataPath,stores,streamStore,rawDataStore,debug,stim)
Type = 'Spike'
Spikes = SpikeClass.Spikes
LFPs = SpikeClass.LFP
SpikeClass.plotSampleWaveform(Spikes,[0])
SpikeClass.plotSampleWaveform(LFPs,[0])
SpikeClass.getLFPSpectrogram([0])
pdb.set_trace()
#filterData = SpikeClass.filterData(Type)
#SpikeClass.extractStimEvents()

