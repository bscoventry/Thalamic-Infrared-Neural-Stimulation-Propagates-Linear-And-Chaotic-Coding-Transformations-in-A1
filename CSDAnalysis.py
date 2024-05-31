#-------------------------------------------------------------------------------------------------------
# Author: Brandon S Coventry
# Date: 05/28/29                       Lovely, cloudy, London-like day in wisco
# Revision Hist: See github
# Purpose: Batch analysis of CSD data.
#-------------------------------------------------------------------------------------------------------
import numpy as np
import scipy.io as sio
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import matplotlib.cm as cm
#Let's do some defs:
def make_plot(xx, yy, zz, title='CSD', cmap=cm.bwr):
    fig = plt.figure(figsize=(7, 7))
    ax = plt.subplot(111)
    ax.set_aspect('equal')
    t_max = np.max(np.abs(zz))
    levels = np.linspace(-1 * t_max, t_max, 32)
    im = ax.contourf(xx, yy, zz, levels=levels, cmap=cmap)
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_title(title)
    ticks = np.linspace(-1 * t_max, t_max, 3, endpoint=True)
    plt.colorbar(im, orientation='horizontal', format='%.2f', ticks=ticks)
    return ax
def parsePW(data):
        
        str1 = data.find("PW")
        str2 = data.find("PU")
        totStr = data[str2:str1+1]
        SplitSTR = totStr.split("_")
        if len(SplitSTR) == 2:
            val = SplitSTR[1]
            val = float(val[0:val.find("P")])
        elif len(SplitSTR) == 3:
            val = SplitSTR[2]
            if val == '1P':
                val = 0.1
            elif val == '2P':
                val = 0.2
            elif val == '3P':
                val = 0.3
            elif val == '4P':
                val = 0.4
            elif val == '5P':
                val = 0.5
            elif val == '6P':
                val = 0.6
            elif val == '7P':
                val = 0.7
            elif val == '8P':
                val = 0.8
            elif val == '9P':
                val = 0.9
            else:
                print('Error in conversion')
        else:
            print(data + ' Error')
        return val
# df1 = pd.read_pickle('LFPCSD0.pkl')
# df2 = pd.read_pickle('LFPCSD1.pkl')
# df3 = pd.read_pickle('LFPCSD3.pkl')
# df4 = df1.append(df2, ignore_index=True)
# df = df4.append(df3, ignore_index=True)
df = pd.read_pickle('testCSD.pkl')
[numrows,numcols] = np.shape(df)
#numrows = 1
EPP = df['EnergyPerPulse']
uniqueEnergy = np.unique(EPP)
ISI = df['ISI']
xarray = df['xarray']
yarray = df['yarray']
maxSink = {}
maxSource = {}
for jk in range(len(uniqueEnergy)):
    maxSink[str(uniqueEnergy[jk])] = []
    maxSource[str(uniqueEnergy[jk])] = []
for ck in range(numrows):
    PW = parsePW(df.DataID[ck])
    ISI = df.ISI[ck]
    nP = df.NPulses[ck]
    stimTime = (nP*PW)+((nP-1)*ISI)
    #Stim window + 100 ms
    stimSamples = int(np.round(stimTime*(1526/1000))+153)
    curCSD = df['estCSD'][ck]
    maxCurrentSinkVec = np.empty((1526,))
    maxCurrentSourceVec = np.empty((1526,))
    for bc in range(1526):
        curcurCSD = curCSD[:,:,bc]
        maxCurrentSinkVec[bc] = np.min(curcurCSD)
        maxCurrentSourceVec[bc] = np.max(curcurCSD)
    maxCurrentSink = np.min(maxCurrentSinkVec[305:305+stimSamples])
    maxCurrentSource = np.max(maxCurrentSourceVec[305:305+stimSamples])
    curEPP = str(EPP[ck])
    maxSink[curEPP].append(maxCurrentSink)
    maxSource[curEPP].append(maxCurrentSource)
    pdb.set_trace()
    [xSink,ySink,tSink] = np.where(curCSD==maxCurrentSink)
    [xSource,ySource,tSource] = np.where(curCSD==maxCurrentSource)
    xSink = xSink[0]
    ySink = ySink[0]
    tSink = tSink[0]
    xSource = xSource[0]
    ySource = ySource[0]
    tSource = tSource[0]
    