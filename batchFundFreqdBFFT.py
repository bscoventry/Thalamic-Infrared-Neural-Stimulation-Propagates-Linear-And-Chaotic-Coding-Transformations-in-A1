import numpy as np
import tdt              #For reading in tdt files
import matplotlib.pyplot as plt
import dask
from SPyke import Spike_Processed
import pdb
import matlab.engine
import pandas as pd
import scipy
import pdb
precurser = 'Z://PhDData//INSData//'
dataPath = ['INS2102//02_15_21//INS_5PU_0_5PW_1ISI','INS2102//02_15_21//INS_5PU_10PW_5ISI','INS2102//02_16_21//INS_5PU_0_2PW_0_1ISI',
            'INS2102//02_16_21//INS_5PU_0_5PW_0_2ISI','INS2102//02_16_21//INS_5PU_0_7PW_0_5ISI','INS2102//02_16_21//INS_5PU_1PW_0_5ISI','INS2102//02_16_21//INS_5PU_5PW_5ISI',
            'INS2102//02_16_21//INS_5PU_5PW_100ISI','INS2102//02_16_21//INS_5PU_10PW_5ISI','INS2102//02_19_21//INS_5PU_10PW_100ISI','INS2102//02_19_21//INS_50PU_0_5PW_0_2ISI',
            'INS2102//02_22_21//INS_5PU_10PW_50ISI_2','INS2102//02_22_21//INS_10PU_0_2PW_0_5ISI','INS2102//02_22_21//INS_10PU_0_2PW_1ISI','INS2102//02_22_21//INS_10PU_0_5PW_1ISI',
            'INS2102//02_22_21//INS_10PU_0_7PW_0_5ISI','INS2102//02_22_21//INS_10PU_1PW_1ISI','INS2102//02_22_21//INS_10PU_5PW_5ISI','INS2102//02_22_21//INS_20PU_0_2PW_0_5ISI',
            'INS2102//02_25_21//INS_5PU_0_7PW_0_5ISI','INS2102//02_25_21//INS_5PU_10PW_50ISI_4','INS2102//02_26_21//INS_5PU_10PW_50ISI','INS2007//08_21_20//INS_5PU_0_2PW_1ISI',
            'INS2007//08_21_20//INS_5PU_0_2PW_5ISI','INS2007//08_21_20//INS_5PU_0_5PW_1ISI','INS2007//08_21_20//INS_5PU_0_5PW_5ISI','INS2007//08_21_20//INS_5PU_1PW_1ISI',
            'INS2007//08_21_20//INS_5PU_1PW_5ISI','INS2007//08_21_20//INS_5PU_0_2PW_1ISI','INS2007//08_21_20//INS_5PU_5PW_5ISI','INS2007//08_24_20//INS_5PU_0_1PW_5ISI',
            'INS2007//08_24_20//INS_5PU_0_2PW_5ISI','INS2007//08_24_20//INS_5PU_0_5PW_5ISI','INS2007//08_24_20//INS_5PU_1PW_5ISI_2','INS2007//08_24_20//INS_5PU_5PW_5ISI','INS2007//08_26_20//INS_5PU_0_2PW_10ISI',
            'INS2007//08_26_20//INS_5PU_0_2PW_100ISI','INS2007//08_26_20//INS_5PU_0_5PW_10ISI','INS2007//08_26_20//INS_5PU_0_5PW_100ISI','INS2007//08_26_20//INS_5PU_1PW_10ISI',
            'INS2007//08_26_20//INS_5PU_1PW_100ISI','INS2007//08_26_20//INS_5PU_5PW_10ISI','INS2007//08_26_20//INS_5PU_5PW_100ISI','INS2007//08_31_20//INS_5PU_0_2PW_5ISI','INS2007//08_31_20//INS_5PU_0_5PW_5ISI',
            'INS2007//08_31_20//INS_5PU_1PW_5ISI_2','INS2007//08_31_20//INS_5PU_1PW_100ISI','INS2007//08_31_20//INS_5PU_5PW_5ISI','INS2007//08_31_20//INS_5PU_5PW_100ISI','INS2007//08_31_20//INS_5PU_10PW_5ISI',
            'INS2007//09_02_20//INS_5PU_0_5PW_20ISI','INS2007//09_02_20//INS_5PU_1PW_1ISI_3','INS2007//09_02_20//INS_5PU_5PW_1ISI','INS2007//09_02_20//INS_5PU_5PW_50ISI','INS2007//09_02_20//INS_5PU_10PW_50ISI',
            'INS2007//09_02_20//INS_5PU_10PW_100ISI','INS2007//09_03_20//INS_5PU_0_1PW_5ISI','INS2007//09_03_20//INS_5PU_0_2PW_5ISI','INS2007//09_03_20//INS_5PU_1PW_1ISI','INS2007//09_03_20//INS_5PU_10PW_50ISI_3',
            'INS2007//09_09_20//INS_5PU_1PW_1ISI','INS2007//09_09_20//INS_5PU_1PW_5ISI','INS2007//09_09_20//INS_5PU_1PW_10ISI','INS2007//09_09_20//INS_5PU_1PW_50ISI','INS2008//08_22_20//INS_5PU_0_2PW_5ISI',
            'INS2008//08_22_20//INS_5PU_0_5PW_5ISI','INS2008//08_22_20//INS_5PU_1PW_1ISI','INS2008//08_22_20//INS_5PU_1PW_5ISI_2','INS2008//08_22_20//INS_5PU_5PW_1ISI','INS2008//08_22_20//INS_5PU_5PW_5ISI_2',
            'INS2008//08_25_20//INS_5PU_0_2PW_100ISI','INS2008//08_25_20//INS_5PU_0_5PW_100ISI','INS2008//08_25_20//INS_5PU_1PW_100ISI','INS2008//08_25_20//INS_5PU_5PW_100ISI','INS2008//08_26_20_2//INS_5PU_0_2PW_5ISI',
            'INS2008//08_26_20_2//INS_5PU_0_2PW_10ISI','INS2008//08_26_20_2//INS_5PU_0_5PW_5ISI','INS2008//08_26_20_2//INS_5PU_0_5PW_10ISI','INS2008//08_26_20_2//INS_5PU_1PW_5ISI',
            'INS2008//08_26_20_2//INS_5PU_1PW_10ISI','INS2008//08_26_20_2//INS_5PU_5PW_5ISI','INS2008//08_26_20_2//INS_5PU_5PW_10ISI','INS2008//09_01_20//INS_5PU_0_2PW_1ISI','INS2008//09_01_20//INS_5PU_0_5PW_1ISI',
            'INS2008//09_01_20//INS_5PU_1PW_1ISI','INS2008//09_01_20//INS_5PU_5PW_1ISI','INS2008//09_01_20//INS_5PU_5PW_5ISI_2','INS2008//09_01_20//INS_5PU_10PW_50ISI','INS2008//09_08_20//INS_5PU_0_1PW_5ISI',
            'INS2008//09_08_20//INS_5PU_0_2PW_5ISI','INS2008//09_08_20//INS_5PU_0_5PW_20ISI','INS2008//09_08_20//INS_5PU_1PW_5ISI','INS2008//09_08_20//INS_5PU_1PW_20ISI','INS2008//09_08_20//INS_5PU_5PW_5ISI',
            'INS2008//09_08_20//INS_5PU_10PW_50ISI_3','INS2013//10_31_20//INS_5PU_1PW_5ISI','INS2013//10_31_20//INS_5PU_0_5PW_5ISI_2','INS2013//10_31_20//INS_5PU_5PW_5ISI','INS2013//10_31_20//INS_5PU_5PW_100ISI_LaserOn',
            'INS2013//11_01_20//INS_5PU_1PW_1ISI','INS2013//11_01_20//INS_5PU_1PW_5ISI','INS2013//11_01_20//INS_5PU_5PW_1ISI','INS2013//11_01_20//INS_5PU_5PW_5ISI','INS2013//11_01_20//INS_5PU_10PW_50ISI',
            'INS2013//11_02_20//INS_5PU_0_5PW_0_3ISI','INS2013//11_02_20//INS_5PU_0_5PW_1ISI','INS2013//11_02_20//INS_5PU_5PW_1ISI','INS2013//11_02_20//INS_5PU_10PW_25ISI','INS2013//11_02_20//INS_5PU_10PW_50ISI_2',
            'INS2013//11_02_20//INS_10PU_0_5PW_0_25ISI','INS2013//11_04_20//INS_1PU_0_2PW_1ISI','INS2013//11_04_20//INS_1PU_0_5PW_1ISI','INS2013//11_04_20//INS_1PU_5PW_50ISI','INS2013//11_04_20//INS_1PU_10PW_50ISI',
            'INS2013//11_04_20//INS_5PU_10PW_50ISI','INS2013//11_04_20//INS_10PU_0_2PW_1ISI','INS2013//11_07_20//INS_5PU_0_2PW_0_2ISI','INS2013//11_07_20//INS_5PU_0_5PW_0_5ISI','INS2013//11_07_20//INS_5PU_1PW_5ISI',
            'INS2013//11_07_20//INS_5PU_10PW_50ISI','INS2013//11_07_20//INS_10PU_1PW_1ISI','INS2013//11_09_20//INS_5PU_0_2PW_0_5ISI','INS2013//11_09_20//INS_5PU_0_5PW_0_5ISI','INS2013//11_09_20//INS_5PU_1PW_0_5ISI',
            'INS2013//11_09_20//INS_10PU_1PW_1ISI_2','INS2013//11_10_20//INS_1PU_0_2PW_1ISI','INS2013//11_10_20//INS_1PU_0_5PW_1ISI','INS2013//11_10_20//INS_1PU_1PW_1ISI','INS2013//11_10_20//INS_1PU_5PW_1ISI','INS2013//11_10_20//INS_1PU_10PW_1ISI',
            'INS2013//11_12_20//INS_10PU_0_2PW_0_5ISI','INS2013//11_12_20//INS_10PU_0_5PW_1ISI','INS2013//11_12_20//INS_10PU_1PW_5ISI','INS2013//11_12_20//INS_10PU_5PW_5ISI','INS2013//11_12_20//INS_10PU_10PW_10ISI',
            'INS2013//11_29_20//INS_5PU_1PW_1ISI','INS2013//11_29_20//INS_5PU_5PW_5ISI','INS2013//11_29_20//INS_5PU_10PW_5ISI','INS2013//11_29_20//INS_5PU_10PW_25ISI','INS2013//11_29_20//INS_5PU_10PW_50ISI',
            'INS2015//11_26_20//INS_1PU_10PW_5ISI','INS2015//11_26_20//INS_5PU_5PW_5ISI','INS2015//11_26_20//INS_5PU_10PW_50ISI','INS2015//11_26_20//INS_10PU_0_5PW_1ISI','INS2015//11_26_20//INS_10PU_1PW_1ISI',
            'INS2015//11_26_20//INS_10PU_1PW_5ISI','INS2015//11_28_20//INS_5PU_1PW_5ISI','INS2015//11_28_20//INS_5PU_5PW_5ISI','INS2015//11_28_20//INS_5PU_10PW_5ISI','INS2015//11_28_20//INS_5PU_10PW_10ISI',
            'INS2015//11_28_20//INS_5PU_10PW_25ISI_2','INS2015//11_28_20//INS_5PU_10PW_50ISI','INS2015//11_30_20//INS_1PU_0_2PW_5ISI','INS2015//11_30_20//INS_1PU_0_5PW_5ISI','INS2015//11_30_20//INS_1PU_1PW_5ISI',
            'INS2015//11_30_20//INS_1PU_5PW_5ISI','INS2015//11_30_20//INS_1PU_10PW_5ISI','INS2015//11_30_20//INS_5PU_10PW_50ISI','INS2015//12_02_20//INS_5PU_0_1PW_5ISI','INS2015//12_02_20//INS_5PU_0_1PW_50ISI',
            'INS2015//12_02_20//INS_5PU_0_2PW_50ISI','INS2015//12_02_20//INS_5PU_0_5PW_50ISI','INS2015//12_02_20//INS_5PU_0_8PW_50ISI','INS2015//12_02_20//INS_5PU_1PW_50ISI','INS2015//12_02_20//INS_5PU_5PW_50ISI',
            'INS2015//12_02_20//INS_5PU_10PW_50ISI','INS2015//12_03_20//INS_5PU_1PW_1ISI','INS2015//12_03_20//INS_5PU_1PW_5ISI','INS2015//12_03_20//INS_5PU_5PW_1ISI','INS2015//12_03_20//INS_5PU_5PW_5ISI',
            'INS2015//12_03_20//INS_5PU_5PW_10ISI','INS2015//12_03_20//INS_5PU_10PW_5ISI','INS2015//12_03_20//INS_5PU_10PW_10ISI','INS2015//12_14_20//INS_5PU_0_5PW_1ISI','INS2015//12_14_20//INS_5PU_5PW_1ISI',
            'INS2015//12_14_20//INS_5PU_10PW_1ISI','INS2015//12_14_20//INS_5PU_10PW_5ISI']               #List of data to sort through
NPulse = [5,5,5,5,5,5,5,5,5,5,50,5,10,10,10,10,10,10,20,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
          5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,1,1,1,1,5,10,5,5,5,5,10,5,5,5,10,1,1,1,1,1,10,
          10,10,10,10,5,5,5,5,5,1,5,5,10,10,10,5,5,5,5,5,5,1,1,1,1,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
PWs = [0.5,10,0.2,0.5,0.7,1,5,5,10,10,0.5,10,0.2,0.2,0.5,0.7,1,5,0.2,0.7,10,10,0.2,0.2,0.5,0.5,1,1,0.2,5,0.1,0.2,0.5,1,5,0.2,0.2,0.5,0.5,1,1,5,5,0.2,0.5,1,1,5,5,10,0.5,1,5,5,10,10,0.1,0.2,1,10,1,1,1,1,0.2,0.5,
       1,1,5,5,0.2,0.5,1,5,0.2,0.2,0.5,0.5,1,1,5,5,0.2,0.5,1,5,5,10,0.1,0.2,0.5,1,1,5,10,1,0.5,5,5,1,1,5,5,10,0.5,0.5,5,10,10,0.5,0.2,0.5,5,10,10,0.2,0.2,0.5,1,10,1,0.2,0.5,1,1,0.2,0.5,1,5,10,0.2,
       0.5,1,5,10,1,5,10,10,10,10,5,10,0.5,1,1,1,5,10,10,10,10,0.2,0.5,1,5,10,10,0.1,0.1,0.2,0.5,0.8,1,5,10,1,1,5,5,5,10,10,0.5,5,10,10]
ISIs = [1,5,0.1,0.2,0.5,0.5,5,100,5,100,0.2,50,0.5,1,1,0.5,1,5,0.5,0.5,50,50,1,5,1,5,1,5,1,5,5,5,5,5,5,10,100,10,100,10,100,10,100,5,5,5,100,5,100,5,20,1,1,50,50,100,5,5,1,50,1,5,10,50,5,5,
        1,5,1,5,100,100,100,100,5,10,5,10,5,10,5,10,1,1,1,1,5,50,5,5,20,5,20,5,50,5,5,5,100,1,5,1,5,50,0.3,1,1,25,50,0.25,1,1,50,50,50,1,0.2,0.5,5,50,1,0.5,0.5,0.5,1,1,1,1,1,1,0.5,
        1,5,5,10,1,5,5,25,50,5,5,50,1,1,5,5,5,5,10,25,50,5,5,5,5,5,50,5,50,50,50,50,50,50,50,1,5,1,5,10,5,10,1,1,1,5]

tISI = np.array(ISIs)*0.001
ISIFreqs = 1/np.array(tISI)

AClass = np.zeros((len(PWs),))
for bc, word1 in enumerate(dataPath):
    if 'INS2102' in word1:
        AClass[bc] = 0
    elif 'INS2007' in word1:
        AClass[bc] = 1
    elif 'INS2008' in word1:
        AClass[bc] = 2
    elif 'INS2013' in word1:
        AClass[bc] = 3
    elif 'INS2015' in word1:
        AClass[bc] = 4
    else:
        print(str(word1)+' is Missed')

df = pd.DataFrame(columns=['DataID', 'Electrode', 'EnergyPerPulse','ISI','NPulses','PW','fundFreq','tMTF'])
#eng = matlab.engine.start_matlab()          #Use the matlab backend for Info theory and Chaos calcs
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
    fundFreq = ISIFreqs[ck]
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
        if fundFreq <= 762:
            SpikeClass = Spike_Processed(precurser+word,NPul,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
            
            #Spikes = SpikeClass.Spikes
            epochedLFP = SpikeClass.sortByStimCondition(SpikeClass.epocLFP)
            ISIMean,ISISD = SpikeClass.getMeanSdEr(epochedLFP)
            
            ISIArrayM = SpikeClass.sortMeanByElectrode16(ISIMean)
            ISIArrayS = SpikeClass.sortMeanByElectrode16(ISISD)
            [ISIArrayM,energy] = SpikeClass.convert2Array(ISIArrayM)
            [ISIArrayS,energy] = SpikeClass.convert2Array(ISIArrayS)
            [ny,nx,nt,ne] = np.shape(ISIArrayM)
            win = (NPul*(PW*0.001))+((NPul-1)*(ISI*0.001))
            
            winSamp = np.round((win*1526))+15
            winSamp = int(winSamp)
            for cmk in range(ny):
                for bc in range(nx):
                    for jk in range(ne):
                        mBaseline = ISIArrayM[cmk,bc,0:305,jk]
                        fourierBaseline = scipy.fft.fft(mBaseline)
                        n = fourierBaseline.size
                        timestep = 1/1526
                        freq = scipy.fft.fftfreq(n, d=timestep)
                        freqWhere = (np.abs(freq - fundFreq)).argmin()
                        basePower = np.absolute(fourierBaseline[freqWhere])

                        stimWin = np.squeeze(ISIArrayM[cmk,bc,305:305+winSamp,jk])
                        fourierStim = scipy.fft.fft(stimWin)
                        n = fourierStim.size
                        timestep = 1/1526
                        freq = scipy.fft.fftfreq(n, d=timestep)
                        freqWhere = (np.abs(freq - fundFreq)).argmin()
                        stimPower = np.absolute(fourierStim[freqWhere])
                        dbChange = 10*np.log10(stimPower/basePower)
                        #maxWhere = np.where(np.abs(dbChange)==np.max(np.abs(dbChange)))
                        #minMaxPower = dbChange[maxWhere]
                        
                        df.loc[-1] = [dataPath,str(SpikeClass.electrodeConfig[cmk,bc]),str(SpikeClass.energyPerPulse[jk]),ISI,NPul,PW,fundFreq,dbChange]
                        df.index = df.index + 1  # shifting index
                        df = df.sort_index()  # sorting by index
        
            df.to_pickle('LFP_tMTF_dB.pkl')
            del SpikeClass             #Just for memory
    except:
        print('Brandon, Check'+' '+word)