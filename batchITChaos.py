#--------------------------------------------------------------------------------------------------------------------------------------------
# Authors: Brandon S Coventry            Wisconsin Institute for Translational Neuroengineering
# Date: 03/5/2024                       Wisconsin is less cold tonight
# Purpose: This is a batch function using SPyke to perform MI/Chaos calculations
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
import matlab.engine
import pandas as pd
dataPath = ['C://DataRepos//INS//INS2102//20210216//5PU_5PW_5ISI']               #List of data to sort through
PWs = [5]
ISIs = [5]
NPulse = [5]
AClass = [5]
df = pd.DataFrame(columns=['DataID', 'Electrode', 'EnergyPerPulse','ISI','NPulses','MI','KChaos','LFPMean','LFPSDER'])
eng = matlab.engine.start_matlab()          #Use the matlab backend for Info theory and Chaos calcs
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
    if AClass[ck] == 5:
        power = np.array((-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414))
    
    SpikeClass = Spike_Processed(word,NPul,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP

    epocedLFPs = SpikeClass.epocTrials(LFPs)
    sortedLFPs = SpikeClass.sortByStimCondition(epocedLFPs)
    for electrode in sortedLFPs.keys():
        curDataElec = sortedLFPs[electrode]
        Rs = np.zeros((12,21))
        R = np.zeros((1,1526))
        counter = 0
        Klist = np.zeros((12,))
        for energies in curDataElec.keys():
            curLFP = curDataElec[energies]
            #[hist,bins] = np.histogram(curLFP,bins=21)       #21 bins from ‘doane’ estimator
            #Rs[counter,:] = matlab.double(hist.tolist())
            R = np.append(R,curLFP,axis=0)
            meanLFP = np.squeeze(np.mean(curLFP,axis=0))
            meanLFP = meanLFP.reshape((1526,1))    # Apparently I need to do this twice...
            meanLFP = matlab.double(meanLFP.tolist())
            [numtrials,nts] = np.shape(curLFP)
            sddvLFP = np.std(curLFP,axis=0)
            sderLFP = sddvLFP/np.sqrt(numtrials)
            K = eng.chaos(meanLFP,0.5,'bvr','schreiber',2,'aaft_cpp','fouda')
            Klist[counter] = K
            counter = counter + 1
            
        R = np.delete(R,0,0)
        
        [Rhist,bins] = np.histogram(R,bins=21)
        Rhist = matlab.double(Rhist.tolist())
        Iarray = np.zeros((12,))
        for bc,energies in enumerate(curDataElec.keys()):
            Rs = curDataElec[energies]
            Rs = matlab.double(Rs.tolist())
            Iqe = eng.MIdrQE(matlab.double(np.transpose(Rs)),matlab.double(np.transpose(R)))
            Iarray[bc] = Iqe
            
            df.loc[-1] = [dataPath,str(electrode),str(energies),ISI,NPul,Iqe,Klist[bc],np.asarray(meanLFP),sderLFP]
            df.index = df.index + 1  # shifting index
            df = df.sort_index()  # sorting by index
        
  

            

    
    del SpikeClass             #Just for memory
pdb.set_trace()