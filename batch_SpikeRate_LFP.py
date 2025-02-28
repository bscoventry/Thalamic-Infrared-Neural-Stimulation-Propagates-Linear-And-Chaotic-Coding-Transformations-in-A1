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
from sklearn.linear_model import LinearRegression
from scipy.integrate import simpson
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

def convert2SpikeRate(spikeArray,stopTime):
    [nTrials,ncols] = np.shape(spikeArray)
    spikeTimes = []
    spontRate = []
    for bc in range(nTrials):
        curTrial = spikeArray[bc,:]

        #Only 1 spike per bin
        spikeLocs=np.where(curTrial>0)
        #convert from samples to time
        spikeLocs = spikeLocs[0]
        curSpikeTimes = spikeLocs/24415.0
        evokedTimes = np.where(np.logical_and(np.greater_equal(curSpikeTimes,0.2),np.less_equal(curSpikeTimes,stopTime + 0.05)))
        evokedTimes = evokedTimes[0]
        spontTimes = np.where(np.less_equal(curSpikeTimes,0.2))
        spontTimes = spontTimes[0]
        spikeCounts = len(evokedTimes)
        spontCounts = len(spontTimes)
        if evokedTimes.size==0:
            spikeCounts = 0
        if spontTimes.size==0:
            spontCounts = 0
        divis = 0.200+(stopTime-0.200+0.05)
        SR = spikeCounts/divis
        sponts = spontCounts/0.2
        spikeTimes.append(SR)
        spontRate.append(sponts)
    return spikeTimes,spontRate

def calcZ(data):
    m = np.mean(data[0:305])
    s = np.std(data[0:305])
    Z = (data-m)/s
    return Z

def calcN1P2(curMLFP,win):
    try:
        #win = int(np.ceil(1526*(stimWin*0.001)))+77            #Add 50ms for offset responses
            
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
                slopeArray=(reg.coef_[0])
                slopeScore=(reg.score(XReg.reshape(-1,1), YReg))
            except:
                pdb.set_trace()
            P2 = P2[0][0]+N1[0][0]
            N1Peak = curMLFP[305+N1[0][0]]
            P2Peak = curMLFP[305+P2]
            N1P2Peak=(np.abs(N1Peak)+np.abs(P2Peak))
            P2 = P2+77              #Plus 50 milliseconds
            integralArray = curMLFP[305:305+P2]
            #AUC.append(simpson(np.abs(integralArray)))
            LFPRMS = (RMS(integralArray))
        else:
            LFPRMS = np.nan
        return LFPRMS
    except:
        pdb.set_trace()

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
def RMS(data):
    return np.sqrt(np.mean(data**2))
def intAUC(data):
    return simpson(data)
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

df = pd.DataFrame(columns=['DataID', 'Electrode', 'EnergyPerPulse','ISI','NPulses','NeuronNumber','N1P2','spkRate','Spont'])
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
    totTime = (NPul*(PW))+((NPul-1)*(ISI))
    win = int(np.ceil(1526*(totTime*0.001)))+77
    endTime = totTime+200
    endTime = endTime*0.001
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
                
                spikeTimes,spontTimes = convert2SpikeRate(curSpikes,endTime)
                curLFP = curLFPset[energy]
                if pk == 0:
                    curLFP = curLFP[0:57,:]
                curLFP = sosfiltfilt(SOS10,curLFP)
                #signal = neo.AnalogSignal(curLFP.T, units='uV',sampling_rate=fs*pq.Hz)
                #stavg = elephant.sta.spike_triggered_average(signal, spikeTimes,(-5 * pq.ms, 10 * pq.ms))
                #To do, SpikeField Coherence, convert each train into a spikeTrain object using neo.SpikeTrain(spiketimes,t_stop=1)
                spikeTimesList = []
                RMSVec = []
                SRVec = []
                SRList = []
                SpontList = []
                for jkt in range(numIter):
                    try:
                        
                        curSpikeTrial = spikeTimes[jkt]
                        #pdb.set_trace()
                        testShape = np.shape(curSpikeTrial)
                        #if testShape[0] >= 0:
                        #pdb.set_trace()
                        #curcurLFP = signal.T
                        curMLFP = curLFP.T[:,jkt]#neo.AnalogSignal(signal[:,jkt],units='uV',sampling_rate=fs*pq.Hz)
                        curSR = spikeTimes[jkt]
                        curSpont = spontTimes[jkt]
                        LFPRMS = calcN1P2(curMLFP,win)
                        SRVec.append(curSR)
                        RMSVec.append(LFPRMS)
                        SpontList.append(curSpont)
                        #phases, amps, times = elephant.phase_analysis.spike_triggered_phase(elephant.signal_processing.hilbert(curLFP),curSpikeTrial,interpolate=True)
                        #sta = elephant.sta.spike_field_coherence(curLFP, curSpikeTrial, (-0.005, 0.010))
    
                            #phaseList.append(phases)
                        
                        
                    except:
                        print('error!')
                        pdb.set_trace()
                df.loc[-1] = [word,aElectrode[ck],energy,ISIs[ck],NPulse[ck],neuron,RMSVec,SRVec,SpontList]
                df.index = df.index + 1  # shifting index
                df = df.sort_index()  # sorting by index
                #df.loc[-1] = [word,aElectrode[ck],energy,ISIs[ck],NPulse[ck],neuron,sfcVec,spikeTimes]
                #df.index = df.index + 1  # shifting index
                #df = df.sort_index()  # sorting by index
    except:
        print('Problem with '+word)
df.to_pickle('SpikeN1P2.pkl')
pdb.set_trace()

