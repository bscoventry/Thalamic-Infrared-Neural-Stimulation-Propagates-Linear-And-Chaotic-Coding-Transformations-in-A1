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
dataPath = 'C://DataRepos//INS//INS2102//20210216//5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
stores = None             #Load all stores
streamStore = 'streams'
rawDataStore = 'TDT2'
debug = 0
stim = 0
Type = 'LFP'
SpksOrLFPs = [Type]
numPulses=5
PW = 5
ISI = 5
power = np.array((-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414))
SpikeClass = Spike_Processed(dataPath,numPulses,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)

#Spikes = SpikeClass.Spikes
LFPs = SpikeClass.LFP

epocedLFPs = SpikeClass.epocTrials(LFPs)
sortedLFPs = SpikeClass.sortByStimCondition(epocedLFPs)
#LFPtest = sortedLFPs['0']
#LFP1 = LFPtest['2.0700000000000003']
LFPmean,LFPsder = SpikeClass.getMeanSdEr(sortedLFPs)
sArray = SpikeClass.sortMeanByElectrode16(LFPmean)
dfDictionary = SpikeClass.convert2DF(sArray)
sampleData = dfDictionary['2.0700000000000003']
cBound = (0,1000)
bBound = (-1000,1000)
pdb.set_trace()
para,bFit = SpikeClass.runWaveFit(sampleData,cBound,bBound)
#SpikeClass.plotSampleWaveform(Spikes,[1])
#SpikeClass.plotSampleWaveform(LFPs,[1])
#Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
pdb.set_trace()
#filterData = SpikeClass.filterData(Type)
#SpikeClass.stimArtifactRemoval(algo='Template')

