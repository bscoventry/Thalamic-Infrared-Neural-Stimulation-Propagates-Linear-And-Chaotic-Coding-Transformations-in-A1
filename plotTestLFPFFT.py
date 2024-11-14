import numpy as np
import tdt              #For reading in tdt files
import matplotlib.pyplot as plt
import dask
from SPyke import Spike_Processed
import pdb

import pandas as pd
import scipy

stores = None             #Load all stores
streamStore = 'streams'
rawDataStore = 'TDT2'
debug = 0
stim = 0
Type = 'LFP'
SpksOrLFPs = [Type]
PW = 5
ISI = 5
fundFreq = 1/(0.005)
NPul = 5
AClass = 4
if AClass == 0:
    power = np.array((-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414))
elif AClass == 1:
    power = np.array((0,4,117,130,143.17,155.9,207,292,357,370,410,431))
elif AClass == 2:
    power = np.array((0,4,117,130,143.17,155.9,207,292,357,370,410,431))
elif AClass == 3:
    power = np.array((-1.1,62.1,77.42,87.4,101.2,115.9,130,184.34,257.3,308.8,360.7,374.4))
elif AClass == 4:
    power = np.array((-1.1,62.1,77.42,87.4,101.2,115.9,130,184.34,257.3,308.8,360.7,374.4))

dPath = 'C:\CodeRepos\SPyke\INS_5PU_1PW_5ISI'
SpikeClass = Spike_Processed(dPath,NPul,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)

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
            if jk == 11:
                pdb.set_trace()