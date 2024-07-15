import numpy as np
import pandas as pd
import neo
import elephant
from scipy import integrate
import matplotlib.pyplot as plt
df = pd.read_pickle('STA.pkl')
nRows = len(df)
dfSTA = pd.DataFrame(columns=['DataID', 'Electrode', 'EnergyPerPulse','ISI','NPulses','NeuronNumber','Trial','STA'])
for ck in range(nRows):
    curSTA = df.STA[ck]
    nReps = len(curSTA)
    for bc in range(nReps):
        curcurSTA = curSTA[bc]
        if len(curcurSTA) > 0:
            RMS = np.sqrt(np.mean(curcurSTA**2))
        else:
            RMS = []
        dfSTA.loc[-1] = [df.DataID[ck],df.Electrode[ck],df.EnergyPerPulse[ck],df.ISI[ck],df.NPulses[ck],df.NeuronNumber[ck],bc,RMS]
        dfSTA.index = dfSTA.index + 1
        dfSTA = dfSTA.sort_index()
dfSTA.to_pickle('AnalyzedSTA.pkl')
ax2 = dfSTA.plot.scatter(x='EnergyPerPulse',y='STA',c='EnergyPerPulse',colormap='viridis')
