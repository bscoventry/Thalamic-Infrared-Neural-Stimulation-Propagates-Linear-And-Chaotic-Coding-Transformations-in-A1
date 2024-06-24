#--------------------------------------------------------------------------------------------------------------------------------
# Author: Brandon S Coventry       Wisconsin Institute for Translational Neuroengineering
# Date: 05/02/2024                 We are having a lovely rainy spring! I'm so stoked!
# Purpose: Batch LFP spike triggered average
# Revision History: See Github
#--------------------------------------------------------------------------------------------------------------------------------
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
import neo
#Include any defs here
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
        curSPK = neo.SpikeTrain(curSpikeTimes,t_stop = 1,units=pq.s)
        spikeTimes.append(curSPK)
    return spikeTimes

def readINSLaserVoltages():
        curVales = loadmat('INSvoltagevals.mat')
        curVales = curVales['stimpeaks']
        [rows,cols] = np.shape(curVales)
        rows = rows-1
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
dfSpikes = pd.read_csv('INS_statTable_STA.csv')#'C:\CodeRepos\SpikeAnalysis\INS_statTable_STA.csv')
[nRows,nCols] = np.shape(dfSpikes)
precurser = 'Z://PhDData//INSData//'
dataPath = []
NPulse = np.empty((nRows,))
PWs = np.empty((nRows,))
ISIs = np.empty((nRows,))
AClass = np.empty((nRows,))
aElectrode = np.empty((nRows,))
SOS10 = loadmat('SOS10')
SOS10 = np.ascontiguousarray(SOS10['SOS'])
for ck in range(nRows):

    curDate = dfSpikes.Date[ck]
    curName = dfSpikes.Name[ck]
    if curName=='INS2102':
        AClass[ck] = 0
    elif curName=='INS2007':
        AClass[ck] = 1
    elif curName=='INS2008':
        AClass[ck] = 2
    elif curName=='INS2013':
        AClass[ck] = 3
    elif curName=='INS2015':
        AClass[ck] = 4
    elif curName=='INS1808':
        AClass[ck] = 5
    elif curName=='INS1806':
        AClass[ck] = 6
    elif curName=='INS1807':
        AClass[ck] = 7
    else:
        print(str(curName)+' is Missed')
        AClass[ck] = np.NaN

    curNPulse = str(dfSpikes.Number_of_Pulses[ck])
    curPW = dfSpikes.Pulse_Width[ck]
    if curPW >= 1:
        curPW = str(round(curPW))
    elif curPW == 0.5:
        curPW = '0_5'
    elif curPW == 0.1:
        curPW = '0_1'
    elif curPW == 0.2:
        curPW = '0_2'
    elif curPW == 0.3:
        curPW = '0_3'
    elif curPW == 0.4:
        curPW = '0_4'
    elif curPW == 0.7:
        curPW = '0_6'
    elif curPW == 0.7:
        curPW = '0_7'
    elif curPW == 0.8:
        curPW = '0_8'
    elif curPW == 0.9:
        curPW = '0_9'

    curISI = dfSpikes.ISI[ck]
    if curISI >= 1:
        curISI = str(round(curISI))
    elif curISI == 0.5:
        curISI = '0_5'
    elif curISI == 0.1:
        curISI = '0_1'
    elif curISI == 0.2:
        curISI = '0_2'
    elif curISI == 0.3:
        curISI = '0_3'
    elif curISI == 0.4:
        curISI = '0_4'
    elif curISI == 0.7:
        curISI = '0_6'
    elif curISI == 0.7:
        curISI = '0_7'
    elif curISI == 0.8:
        curISI = '0_8'
    elif curISI == 0.9:
        curISI = '0_9'
    elif curISI == 0.0:
        curISI = '0'

    aElectrode[ck] = dfSpikes.Electrode_Number[ck]-1    #-1 to account for python numbering
    curDataPath = curName+'//'+curDate+'//INS_'+curNPulse+'PU_'+curPW+'PW_'+curISI+'ISI'
    dataPath.append(curDataPath)
    NPulse[ck] = float(curNPulse)
    PWs[ck] = float(curPW)
    ISIs[ck] = float(curISI)
fs = 1526
uniqueVals = readINSLaserVoltages()

df = pd.DataFrame(columns=['DataID', 'Electrode', 'EnergyPerPulse','ISI','NPulses','NeuronNumber','STA','SFC','SFC_Freqs','STP','spkTimes'])
curWord = 'start'
for ck, word in enumerate(dataPath):
    stores = None             #Load all stores
    streamStore = 'streams'
    rawDataStore = 'TDT2'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    PW = PWs[ck]
    ISI = ISIs[ck]
    NPul = NPulse[ck]
    if AClass[ck] == 0:
        power = np.array((-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414))
    elif AClass[ck] == 1:
        power = np.array((0,4,117,130,143.17,155.9,207,292,357,370,410,431))
    elif AClass[ck] == 2:
        power = np.array((0,4,117,130,143.17,155.9,207,292,357,370,410,431))
    elif AClass[ck] == 3:
        power = np.array((-1.1,62.1,77.42,87.4,101.2,115.9,130,184.34,257.3,308.8,360.7,374.4))
    elif AClass[ck] == 4:
        power = np.array((-1.1,62.1,77.42,87.4,101.2,115.9,130,184.34,257.3,308.8,360.7,374.4))
    try:
        if word!=curWord:
            SpikeClass = Spike_Processed(precurser+word,NPul,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
            LFPs = SpikeClass.LFP

            epocedLFPs = SpikeClass.epocTrials(LFPs)
            sortedLFPs = SpikeClass.sortByStimCondition(epocedLFPs)
            #Now that we have LFPs, load in Spikes
            spikeRaster1 = mat73.loadmat(precurser+word+'//spikeSortRaster1.mat')
            spikeRaster1 = spikeRaster1['spikeSortRaster1']
            #Shape of each is (8,). Inside this is the shape (n_neurons,n_trials,n_timesteps)
            spikeRaster2 = mat73.loadmat(precurser+word+'//spikeSortRaster2.mat')
            spikeRaster2 = spikeRaster2['spikeSortRaster2']
            spikeRaster = spikeRaster1+spikeRaster2 #Is now (16,) in size.
            #for electrode in sortedLFPs.keys():
            curWord = word
        curLFPset = sortedLFPs[str(int(aElectrode[ck]))]
        curSpikeRaster = spikeRaster[int(aElectrode[ck])]
        [nNeurons,nTrials,nTS] = np.shape(curSpikeRaster)
        for neuron in range(nNeurons):
            curRaster = curSpikeRaster[neuron]
            for pk,energy in enumerate(curLFPset.keys()):

                curSpikes = curRaster[uniqueVals[str(pk)],:]
                [numIter,dnc] = np.shape(curSpikes)
                spikeTimes = convert2SpikeTime(curSpikes)
                curLFP = curLFPset[energy]
                if pk == 0:
                    curLFP = curLFP[0:57,:]
                curLFP = sosfiltfilt(SOS10,curLFP)
                signal = neo.AnalogSignal(curLFP.T, units='uV',sampling_rate=fs*pq.Hz)
                stavg = elephant.sta.spike_triggered_average(signal, spikeTimes,(-5 * pq.ms, 10 * pq.ms))
                #To do, SpikeField Coherence, convert each train into a spikeTrain object using neo.SpikeTrain(spiketimes,t_stop=1)
                spikeTimesList = []
                freqVec = []
                sfcVec = []
                phaseList = []

                for jkt in range(numIter):
                    try:
                        curSpikeTrial = spikeTimes[jkt]
                        testShape = np.shape(curSpikeTrial)
                        if testShape[0] != 0:
                            #curcurLFP = signal.T
                            curLFP = neo.AnalogSignal(signal[:,jkt],units='uV',sampling_rate=fs*pq.Hz)
                            phases, amps, times = elephant.phase_analysis.spike_triggered_phase(elephant.signal_processing.hilbert(curLFP),curSpikeTrial,interpolate=True)
                            sfc, freqs = elephant.sta.spike_field_coherence(curLFP, curSpikeTrial, window='boxcar')
                            sfcVec.append(sfc)
                            freqVec.append(freqs)
                            phaseList.append(phases)
                    except:
                        print('error!')
                        pdb.set_trace()
                df.loc[-1] = [word,aElectrode[ck],energy,ISIs[ck],NPulse[ck],neuron,stavg,sfcVec,freqVec,phaseList,spikeTimes]
                df.index = df.index + 1  # shifting index
                df = df.sort_index()  # sorting by index
    except:
        print('Problem with '+word)
df.to_pickle('STA.pkl')
pdb.set_trace()
