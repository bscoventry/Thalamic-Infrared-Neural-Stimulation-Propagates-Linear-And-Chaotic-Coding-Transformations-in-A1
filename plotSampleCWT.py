import numpy as np
import tdt              #For reading in tdt files
import matplotlib.pyplot as plt
import dask
from SPyke import Spike_Processed
import pdb
import fcwt
import pandas as pd
import scipy

stores = None             #Load all stores
streamStore = 'streams'
rawDataStore = 'TDT2'
debug = 0
stim = 0
Type = 'LFP'
SpksOrLFPs = [Type]
PW = 10
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

dPath = 'C:\CodeRepos\SPyke\INS2015_1128'
SpikeClass = Spike_Processed(dPath,NPul,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
#Spikes = SpikeClass.Spikes
epochedLFP = SpikeClass.sortByStimCondition(SpikeClass.epocLFP)
channel = 10
LFP = epochedLFP[str(channel)]
#pdb.set_trace()
ener = '3.0880000000000005'
LFPE = LFP[ener]
curTrial = 5
f0 = 3 #lowest frequency
f1 = 200 #highest frequency
fn = 1000 #number of frequencies
freqs, out = fcwt.cwt(np.squeeze(LFPE[curTrial,:]), 1526, f0, f1, fn)
out = np.abs(out)
ts = np.arange(0,1,1/1526)
mbaseline = np.mean(out[:,0:305],axis=1)
#dBChange = out
#dBChange = np.transpose(out)
dBChange = np.transpose(out)/mbaseline
#dBChange = np.transpose(dBChange)
#dBChange = np.log(dBChange)
dBChange = 10*np.log10(np.transpose(dBChange))
#dBChange = dBChange/np.max(dBChange)
plt.contourf(ts,freqs,dBChange)
plt.colorbar()
win = (NPul*(PW*0.001))+((NPul-1)*(ISI*0.001))
winSamp = np.round((win*1526))+15
winSamp = int(winSamp)
plt.hlines(200.5,0.2,0.270)
plt.show()
pdb.set_trace()