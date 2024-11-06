import numpy as np
import scipy.io as sio
import pandas as pd
import pdb
import matplotlib.pyplot as plt

df = pd.read_pickle('LFP_tMTF.pkl')

nRows = len(df)
mTMTFm = np.zeros((nRows,))
mTMTFs = np.zeros((nRows,))
for ck in range(nRows):
    curtMTF = df.tMFT[ck]
    curtMTFs = df.tMTFS[ck]
    mTMTFm[ck] = 10*np.log10(np.max(curtMTF)/curtMTF[0])

df["mTMTFm"] = mTMTFm
uniqueFreq = np.unique(df.fundFreq)
uniqueFreq = np.delete(uniqueFreq,-1)
histBins = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
histBins = np.array(histBins)

histLoc = np.zeros((len(df.EnergyPerPulse)))

for ck in range(len(df.EnergyPerPulse)):
    curE = df.EnergyPerPulse[ck]
    curE = float(curE)
    if curE <= 0.5:
        index = 0
    elif curE > 0.5 and curE <= 1:
        index = 1
    elif curE > 1 and curE <= 1.5:
        index = 2
    elif curE > 1.5 and curE <= 2:
        index = 3
    elif curE > 2 and curE <= 2.5:
        index = 4
    elif curE > 2.5 and curE <= 3:
        index = 5
    elif curE > 3 and curE <= 3.5:
        index = 6
    elif curE > 3.5 and curE <= 4:
        index = 7
    elif curE > 4:
        index = 8
    histLoc[ck] = index
df["histLoc"] = histLoc
df['logTMTF'] = np.log(mTMTFm+0.001)
for ck in range(len(uniqueFreq)):
    curFreq = uniqueFreq[ck]
    curDF = df.loc[df['fundFreq'] == curFreq]
    curDF.reset_index(drop=True, inplace = True)
    
    curDF.boxplot(column = 'mTMTFm',by='histLoc')
    plt.title(str(curFreq))
    plt.show()
    

