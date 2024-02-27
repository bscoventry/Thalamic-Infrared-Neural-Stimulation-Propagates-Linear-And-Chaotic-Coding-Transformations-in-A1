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
#LFPmean,LFPsder = SpikeClass.getMeanSdEr(SpikeClass.epocedAlpha)
alphaMean,alphaSD = SpikeClass.getMeanSdEr(SpikeClass.epocedAlpha)
betaMean,betaSD = SpikeClass.getMeanSdEr(SpikeClass.epochedBeta)
thetaMean,thetaSD = SpikeClass.getMeanSdEr(SpikeClass.epochedTheta)
lgMean,lgSD = SpikeClass.getMeanSdEr(SpikeClass.epochedLowGamma)
hgMean,hgSD = SpikeClass.getMeanSdEr(SpikeClass.epochedHighGamma)
alphaArrayM = SpikeClass.sortMeanByElectrode16(alphaMean)
alphaArrayS = SpikeClass.sortMeanByElectrode16(alphaSD)
betaArrayM = SpikeClass.sortMeanByElectrode16(betaMean)
betaArrayS = SpikeClass.sortMeanByElectrode16(betaSD)
thetaArrayM = SpikeClass.sortMeanByElectrode16(thetaMean)
thetaArrayS = SpikeClass.sortMeanByElectrode16(thetaSD)
lgArrayM = SpikeClass.sortMeanByElectrode16(lgMean)
lgArrayS = SpikeClass.sortMeanByElectrode16(lgSD)
hgArrayM = SpikeClass.sortMeanByElectrode16(hgMean)
hgArrayS = SpikeClass.sortMeanByElectrode16(hgSD)
[alphaArrayM,energy] = SpikeClass.convert2Array(alphaArrayM)
[alphaArrayS,energy] = SpikeClass.convert2Array(alphaArrayS)
[betaArrayM,energy] = SpikeClass.convert2Array(betaArrayM)
[betaArrayS,energy] = SpikeClass.convert2Array(betaArrayS)
[thetaArrayM,energy] = SpikeClass.convert2Array(thetaArrayM)
[thetaArrayS,energy] = SpikeClass.convert2Array(thetaArrayS)
[lgArrayM,energy] = SpikeClass.convert2Array(lgArrayM)
[lgArrayS,energy] = SpikeClass.convert2Array(lgArrayS)
[hgArrayM,energy] = SpikeClass.convert2Array(hgArrayM)
[hgArrayS,energy] = SpikeClass.convert2Array(hgArrayS)
saveArray = {'alphaMean':alphaArrayM,'alphaSD':alphaArrayS,'betaMean':betaArrayM,'betaSD':betaArrayS,'thetaMean':thetaArrayM,'thetaSD':thetaArrayS,'lowGammaMean':lgArrayM,'lowGammaSD':lgArrayS,'highGammaMean':hgArrayM,'highGammaSD':lgArrayS,'Energy':energy}
#LFPCOG = SpikeClass.COG(sArray)
pdb.set_trace()
SpikeClass.plotCOG(LFPCOG['2.0700000000000003'])
dfDictionary = SpikeClass.convert2DF(sArray)
sampleData = dfDictionary['2.0700000000000003']
cBound = (0,5)
bBound = (-100,100)

para,bFit = SpikeClass.runWaveFit(sampleData,cBound,bBound)
#SpikeClass.plotSampleWaveform(Spikes,[1])
#SpikeClass.plotSampleWaveform(LFPs,[1])
#Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
pdb.set_trace()
#filterData = SpikeClass.filterData(Type)
#SpikeClass.stimArtifactRemoval(algo='Template')

