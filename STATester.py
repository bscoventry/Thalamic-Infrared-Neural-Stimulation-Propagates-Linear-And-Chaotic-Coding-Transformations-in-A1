#---------------------------------------------------------------------------------------
#Author: Brandon S Coventry
# This is just testing/playing with elephant's STA Analysis. Not used for actual data.
#---------------------------------------------------------------------------------------
import elephant
import tdt              #For reading in tdt files
import matplotlib.pyplot as plt
import dask
from SPyke import Spike_Processed
import pdb
import pandas as pd
import numpy as np
from scipy.io import loadmat
from datetime import datetime, date, time
from scipy.signal import sosfiltfilt
import mat73
import quantities as pq
import os
import neo
def convert2SpikeTime(spikeArray):

    [nTrials,ncols] = np.shape(spikeArray)
    spikeTimes = []
    for bc in range(nTrials):
        curTrial = spikeArray[bc,:]

        #Only 1 spike per bin
        spikeLocs=np.where(curTrial>0)
        #convert from samples to time
        spikeLocs = spikeLocs[0]
        curSpikeTimes = spikeLocs/24415.0
        spikeTimes.append(curSpikeTimes)
    return spikeTimes

def readINSLaserVoltages():
        curVales = loadmat('INSvoltagevals.mat')
        curVales = curVales['stimpeaks']
        [rows,cols] = np.shape(curVales)
        rows=rows-1
        voltageVals = np.zeros((rows,))

        for ck in range(rows):

            voltageVals[ck] = curVales[ck][0]
        #self.voltageVals = voltageVals
        uniqueVals = np.unique(voltageVals)
        #Get energy per pulse
        #self.energyPerPulse = (self.power*0.001)*(self.PW*0.001)*1000

        numUnique = len(uniqueVals)
        uniqueWhere = {}

        for bc in range(numUnique):
            curUniq = uniqueVals[bc]
            #curEnergy = self.energyPerPulse[bc]
            uniWhere = np.argwhere(curUniq==voltageVals)
            numT = len(uniWhere)
            indArray = []
            for jvk in range(numT):
                indArray.append(uniWhere[jvk][0])
            uniqueWhere[str(bc)] = indArray
        return uniqueWhere
pwd=os.getcwd()
power = np.array((-1.1,62.1,77.42,87.4,101.2,115.9,130,184.34,257.3,308.8,360.7,374.4))
stores = None             #Load all stores
streamStore = 'streams'
rawDataStore = 'TDT2'
debug = 0
stim = 0
Type = 'LFP'
SpksOrLFPs = [Type]
fs = 1526.0
SOS10 = loadmat('SOS10')
SOS10 = np.ascontiguousarray(SOS10['SOS'])
SpikeClass = Spike_Processed(pwd,5,10,5,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
LFPs = SpikeClass.LFP
uniqueVals = readINSLaserVoltages()
epocedLFPs = SpikeClass.epocTrials(LFPs)
sortedLFPs = SpikeClass.sortByStimCondition(epocedLFPs)
#Now that we have LFPs, load in Spikes
spikeRaster1 = mat73.loadmat('spikeSortRaster1.mat')
spikeRaster1 = spikeRaster1['spikeSortRaster1']
#Shape of each is (8,). Inside this is the shape (n_neurons,n_trials,n_timesteps)
spikeRaster2 = mat73.loadmat('spikeSortRaster2.mat')
spikeRaster2 = spikeRaster2['spikeSortRaster2']
spikeRaster = spikeRaster1+spikeRaster2 #Is now (16,) in size.
#for electrode in sortedLFPs.keys():

curLFPset = sortedLFPs[str(1)]
curSpikeRaster = spikeRaster[1]
[nNeurons,nTrials,nTS] = np.shape(curSpikeRaster)
testKeys = ['3.744']
for neuron in range(nNeurons):

    curRaster = curSpikeRaster[neuron]
    for pk,energy in enumerate(testKeys):

        curSpikes = curRaster[uniqueVals[str(pk)],:]
        spikeTimes = convert2SpikeTime(curSpikes)

        curLFP = curLFPset[energy]
        if pk == 0:
            curLFP = curLFP[0:57,:]
        curLFP = sosfiltfilt(SOS10,curLFP)
        pdb.set_trace()
        [lfpRows,lfpcols] = np.shape(curLFP)

        signal = neo.AnalogSignal(curLFP.T, units='uV',sampling_rate=fs*pq.Hz)
        stavg = elephant.sta.spike_triggered_average(signal, spikeTimes,(-5 * pq.ms, 10 * pq.ms))
        #To do, SpikeField Coherence, convert each train into a spikeTrain object using neo.SpikeTrain(spiketimes,t_stop=1)
        spikeTimesList = []
