import numpy as np
import pandas as pd
import neo
import elephant
from scipy import integrate
import matplotlib.pyplot as plt
from pycircstat.tests import rayleigh
df = pd.read_pickle('STP.pkl')
nRows = len(df)
dfSTA = pd.DataFrame(columns=['DataID', 'Electrode', 'EnergyPerPulse','ISI','NPulses','NeuronNumber','Trial','neuronNumber','STC'])
for ck in range(nRows):
    curSTA = df.STC[ck]
    nReps = len(curSTA)
    for bc in range(nReps):
        curcurSTA = curSTA[bc]
        if len(curcurSTA) > 0:
            phase = curcurSTA
            for jk in range(len(phase)):
                dfSTA.loc[-1] = [df.DataID[ck],df.Electrode[ck],df.EnergyPerPulse[ck],df.ISI[ck],df.NPulses[ck],df.NeuronNumber[ck],bc,jk,phase[jk]]
                dfSTA.index = dfSTA.index + 1
                dfSTA = dfSTA.sort_index()
dfSTA.to_pickle('AnalyzedSTA.pkl')
#ax2 = dfSTA.plot.scatter(x='EnergyPerPulse',y='STC',c='EnergyPerPulse',colormap='viridis')
dfSTA.boxplot(column=['STC'],by='EnergyPerPulse')
EPP = dfSTA.EnergyPerPulse.values
STC_EPP = {}
uniqueEPP = np.unique(EPP)
pValues = np.zeros((len(uniqueEPP)),)
for ck in range(len(uniqueEPP)):
    curEPP = uniqueEPP[ck]
    curSTC = dfSTA.STC.loc(dfSTA[EPP]==curEPP)
    #STC_EPP[str(curEPP)] = dfSTA.STC.loc(dfSTA[EPP]==curEPP)
    [p,z] = rayleigh(curSTC)
    pValues[ck] = p
pdb.set_trace()



