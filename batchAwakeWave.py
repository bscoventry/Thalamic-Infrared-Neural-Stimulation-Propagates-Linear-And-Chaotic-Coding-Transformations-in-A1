#--------------------------------------------------------------------------------------------------------------------------------------------
# Authors: Brandon S Coventry            Wisconsin Institute for Translational Neuroengineering
# Date: 03/22/2024                       Still snowing... It's spring and it's still snowing...
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
precurser = 'Z://PhDData//INSData//'
dataPath = ['INS1808//4_18_18//INS_5V_5ms','INS1808//4_18_18//INS_5V_10ms','INS1808//4_19_18_2//INS_4V_20ms_3','INS1808//4_20_18//INS_2V_5ms','INS1808//4_20_18//INS_2V_20ms',
            'INS1808//4_20_18//INS_3V_20ms','INS1808//4_20_18//INS_5V_5ms','INS1808//4_20_18//INS_5V_200us','INS1808//4_23_18//INS_4V_20ms','INS1808//4_24_18//INS_4V_20ms',
            'INS1806//4_16_18//INS_5V_5ms_2']               #List of data to sort through
NPulse = [1,1,1,1,1,1,1,1,1,1,1]
PWs = [5,10,20,5,20,20,1,0.2,20,20,5]
ISIs = [0,0,0,0,0,0,0,0,0,0,0]
Energy = [3.3,6,10.5,1.125,4.5,7.4,3.3,0.12,10.5,10.5,3]
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
    Energy = [ck]
    df = pd.DataFrame(columns=['DataID','EnergyPerPulse','ISI','NPulses','Velocity','WaveTransistion','prctSVD'])
    eng = matlab.engine.start_matlab()          #Use the matlab backend for Info theory and Chaos calcs
    fs = 1526
    try:
        SpikeClass = Spike_Processed(precurser+word,NPul,PW,ISI,Energy,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)

        #Spikes = SpikeClass.Spikes
        LFPs = SpikeClass.LFP

        epocedLFPs = SpikeClass.epocTrials(LFPs)
        sorted = SpikeClass.sortByElectrode16_MonoEnergy(epocedLFPs)
        curLFP = sorted
        curLFP = matlab.double(curLFP.tolist())
        mWaveVel,transitionMatrix,prctVar = eng.batchWavePatt(curLFP,fs,nargout=3)
        df.loc[-1] = [word,Energy,ISI,NPul,mWaveVel,transitionMatrix,prctVar]
        df.index = df.index + 1  # shifting index
        df = df.sort_index()  # sorting by index
    except Exception as error:
        # handle the exception
        print("An exception occurred:", type(error).__name__, "–", error) # An exception occurred: ZeroDivisionError – division by zero
        print('Brandon, check'+' '+word)
df.to_pickle('LFPChaosAwake.pkl')
pdb.set_trace()
        
