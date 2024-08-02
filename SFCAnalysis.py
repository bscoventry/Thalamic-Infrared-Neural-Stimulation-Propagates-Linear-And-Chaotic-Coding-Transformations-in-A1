import numpy as np
import scipy.io as sio
import pandas as pd
import pdb
import matplotlib.pyplot as plt
def addLabelsToDF(df):
    EPP = df.EnergyPerPulse.values
    
    nRows = len(EPP)
    labels = np.zeros((nRows,),dtype=int)
    for ck in range(nRows):
        
        if float(EPP[ck]) <0.5:
            labels[ck] = 0
        elif 0.5<= float(EPP[ck]) < 1: 
            labels[ck] = 1
        elif 1<= float(EPP[ck]) < 1.5: 
            labels[ck] = 2
        elif 1.5<= float(EPP[ck]) < 2: 
            labels[ck] = 3
        elif 2<= float(EPP[ck]) < 2.5: 
            labels[ck] = 4
        elif 2.5<= float(EPP[ck]) < 3: 
            labels[ck] = 5
        elif 3<= float(EPP[ck]) < 3.5: 
            labels[ck] = 6
        elif float(EPP[ck])>=3.5: 
            labels[ck] = 7
    df['labels'] = labels
    return df

df = pd.read_pickle('SFC.pkl')
df = addLabelsToDF(df)
freqs = sio.loadmat('SFCFreqs.mat')
freqs = freqs['freqs']
freqs = np.squeeze(freqs)
freqsWhere = np.where(freqs<=200)
freqsWhere = freqsWhere[0]
nRows = len(df)
thetaCoh = np.nan*np.ones((nRows,))
alphaCoh = np.nan*np.ones((nRows,))
betaCoh = np.nan*np.ones((nRows,))
lgCoh = np.nan*np.ones((nRows,))
hgCoh = np.nan*np.ones((nRows,))
freqVec = np.nan*np.ones((nRows,))
labels = df.labels.values
for ck in range(nRows):
    curSFC = df.meanSFC[ck]
    curSFC = curSFC[freqsWhere]
    thetaCoh[ck] = curSFC[1]
    alphaCoh[ck] = curSFC[2]
    betaCoh[ck] = np.max(curSFC[3:6])
    #betaCoh[ck] = np.max(curSFC[3])
    lgCoh[ck] = np.max(curSFC[6:14])
    #lgCoh[ck] = np.max(curSFC[6])
    hgCoh[ck] = np.max(curSFC[14:34])
    #hgCoh[ck] = np.max(curSFC[14])
    maxSFC = np.nanmax(curSFC)
    
    freqLoc = np.where(curSFC==maxSFC)
    freqVec[ck] = freqsWhere[freqLoc]

df['thetaCoh'] = thetaCoh
df['alphaCoh'] = alphaCoh
df['betaCoh'] = betaCoh
df['lgCoh'] = lgCoh
df['hgCoh'] = hgCoh
df['freqVec'] = freqVec
fig, axes = plt.subplots(2,3)

EPP = df.EnergyPerPulse.values
EPP = [float(i) for i in EPP]
EPP = np.array(EPP)
EPP[EPP<=0] = 0

lepp = np.log(EPP+0.001)
lepp[lepp<=-4.5] = np.nan
df['lepp'] = lepp
for bc in range(5):
    if bc == 0:
        #df.boxplot(column='thetaCoh',by='labels',ax=axes.flatten()[bc])
        df.plot.scatter(y='thetaCoh',x='lepp',ax=axes.flatten()[bc])
        axes.flatten()[bc].set_title('Theta')
        axes.flatten()[bc].set_ylim([-0.05, 1])
    if bc == 1:
        #df.boxplot(column='alphaCoh',by='labels',ax=axes.flatten()[bc])
        df.plot.scatter(y='alphaCoh',x='lepp',ax=axes.flatten()[bc])
        axes.flatten()[bc].set_title('Alpha')
        axes.flatten()[bc].set_ylim([-0.05, 1])
    if bc == 2:
        #df.boxplot(column='betaCoh',by='labels',ax=axes.flatten()[bc])
        df.plot.scatter(y='betaCoh',x='lepp',ax=axes.flatten()[bc])
        axes.flatten()[bc].set_title('Beta')
        axes.flatten()[bc].set_ylim([-0.05, 1])
    if bc == 3:
        #df.boxplot(column='lgCoh',by='labels',ax=axes.flatten()[bc])
        df.plot.scatter(y='lgCoh',x='lepp',ax=axes.flatten()[bc])
        axes.flatten()[bc].set_title('Low Gamma')
        axes.flatten()[bc].set_ylim([-0.05, 1])
    if bc == 4:
        #df.boxplot(column='hgCoh',by='labels',ax=axes.flatten()[bc])
        df.plot.scatter(y='hgCoh',x='lepp',ax=axes.flatten()[bc])
        axes.flatten()[bc].set_title('High Gamma')
        axes.flatten()[bc].set_ylim([-0.05, 1])
#df.plot.scatter(y='freqVec',x='lepp')
pdb.set_trace()