import elephant
import neo
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from SPyke import Spike_Processed
import pdb
import mat73
import quantities as pq
def convert2SpikeTime(spikeArray):

    [nTrials,ncols] = np.shape(spikeArray)
    spikeTimes = []
    #for bc in range(nTrials):
    curTrial = spikeArray

    #Only 1 spike per bin
    spikeLocs=spikeArray
    #convert from samples to time
    
    spikeLocs = spikeLocs[0][0]
    curSpikeTimes = spikeLocs/24415.0
    curSPK = neo.SpikeTrain([curSpikeTimes],t_stop = 1,units=pq.s)
    spikeTimes.append(curSPK)
    return spikeTimes
Spikes = mat73.loadmat('INS_5PU_1PW_5ISI\spikeSortRaster1.mat')
Spikes = Spikes['spikeSortRaster1']
Spikes = Spikes[1]
Spikes = Spikes[1][31,:]
power = np.array((-1.1,62.1,77.42,87.4,101.2,115.9,130,184.34,257.3,308.8,360.7,374.4))
stores = None
streamStore = 'streams'
debug = 0
stim = 0
Type = 'LFP'
SpksOrLFPs = [Type]
SpikeClass= Spike_Processed('INS_5PU_1PW_5ISI',5,1,5,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
LFPs = SpikeClass.LFP
epocedLFPs = SpikeClass.epocTrials(LFPs)
eLFPs = epocedLFPs['1']
tLFP = eLFPs[31,:]
tsSpikes = np.arange(0,1,1/24415)
tsSpikes = tsSpikes[tsSpikes<=0.27]
tsLFPs = np.arange(0,1,1/1526)
tsLFPs = tsLFPs[tsLFPs<=0.27]
signal = neo.AnalogSignal(tLFP.T, units='uV',sampling_rate=1526*pq.Hz)
SpikeTimes = np.where(Spikes==1)
#SpikeTimes = SpikeTimes[0][0]
#SpikeTimes = SpikeTimes/24415
ST = convert2SpikeTime(SpikeTimes)

STA = elephant.sta.spike_triggered_average(signal, ST,(-100 * pq.ms, 0 * pq.ms))
tLFP = tLFP[0:len(tsLFPs)]
nSpikes = Spikes*(np.max(tLFP)-np.min(tLFP))+np.min(tLFP)
nSpikes = nSpikes[0:len(tsSpikes)]
#fig,axes = plt.subplot(2,1)
tSTA = np.arange(-.100,0,1/1526)
tLFP = tLFP[0:len(tsLFPs)]
stimLineTime = [.200,.225]
stimLine = 0.000055*np.ones((len(stimLineTime),))
plt.subplot(2,1,1)
plt.plot(tsLFPs,(tLFP),(tsSpikes),nSpikes)
#plt.plot(stimLineTime,stimLine,'r')
plt.stem(stimLineTime,(stimLine),'-r')
plt.subplot(2,1,2)
STAvec = np.min(tLFP)*np.ones((len(tLFP),))
tsWhere = np.where(np.abs(tsLFPs-0.20860127)==np.min(np.abs(tsLFPs-0.20860127)))
tsWhere = tsWhere[0][0]
STAvec[tsWhere-len(tSTA):tsWhere] = np.squeeze(STA)
RMS = np.sqrt(np.nanmean(np.squeeze(STA)**2))
print(RMS)
plt.plot(tsLFPs,(STAvec))
plt.show()
pdb.set_trace()
