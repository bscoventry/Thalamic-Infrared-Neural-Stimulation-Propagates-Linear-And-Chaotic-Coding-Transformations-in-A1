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

df = pd.read_pickle('STA.pkl')
df = addLabelsToDF(df)
uniqueISIs = np.unique(df.ISI.values)
numISIs = len(uniqueISIs)
fig, axes = plt.subplots(2,4)
maxSTA = np.nanmax(df.STAMeanAUC.values)+0.000005

for ck in range(numISIs):
    dfSamp = df.loc[df.ISI==uniqueISIs[ck]]
    dfSamp.boxplot(column='STAMeanAUC',by='labels',ax=axes.flatten()[ck])
    axes.flatten()[ck].set_title(str(uniqueISIs[ck]))
    axes.flatten()[ck].set_ylim([0, maxSTA])
#df.boxplot(column='STAMeanAUC',by='labels')
#df.boxplot(column='STASdERAUC',by='labels')
plt.show()