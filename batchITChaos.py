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
    SpikeClass = Spike_Processed(dataPath,NPul,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP

    epocedLFPs = SpikeClass.epocTrials(LFPs)
    sortedLFPs = SpikeClass.sortByStimCondition(epocedLFPs)