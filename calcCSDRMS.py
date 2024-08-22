import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import pdb
def addLabelsToDF(df):
    EPP = df.EnergyPerPulse.values
    nRows = len(EPP)
    labels = np.zeros((nRows,),dtype=int)
    for ck in range(nRows):
        if EPP[ck] <0.5:
            labels[ck] = 0
        elif 0.5<= EPP[ck] < 1: 
            labels[ck] = 1
        elif 1<= EPP[ck] < 1.5: 
            labels[ck] = 2
        elif 1.5<= EPP[ck] < 2: 
            labels[ck] = 3
        elif 2<= EPP[ck] < 2.5: 
            labels[ck] = 4
        elif 2.5<= EPP[ck] < 3: 
            labels[ck] = 5
        elif 3<= EPP[ck] < 3.5: 
            labels[ck] = 6
        elif EPP[ck]>=3.5: 
            labels[ck] = 7
    df['labels'] = labels
    return df
data = pd.read_pickle('CSDTrain.pkl')
data = addLabelsToDF(data)
Sinks = data['Sinks']
Sources = data['Sources']
nrows = len(data)
RMS = np.zeros((nrows,))
EPP = data.EnergyPerPulse.values
EPP[EPP<=0] = 0
lepp = np.log(EPP+0.001)
data = data.assign(lepp=lepp)
data = data.assign(RMSSink=RMS)
data = data.assign(RMSSource=RMS)

for ck in range(nrows):
    curSink = Sinks[ck]
    data.RMSSink[ck] = np.sqrt(np.mean(curSink**2))
    if data.RMSSink[ck]>0.010:
        data.RMSSink[ck] = np.NaN
    curSource = Sources[ck]
    data.RMSSource[ck] = np.sqrt(np.mean(curSource**2))
data.plot.scatter(x='lepp',y='RMSSink')
plt.show()
data.plot.scatter(x='lepp',y='RMSSource')
plt.show()
data.to_pickle('CSD_DF.pkl')