import pymc as pm
import numpy as np
import arviz as az
import matplotlib.pyplot as plt
import pdb
import pandas as pd

rTrace = az.from_netcdf('spikeN1P2Regression.netcdf')
aPost = rTrace.posterior.a.values.flatten()
b1Post = rTrace.posterior.b1.values.flatten()
b2Post = rTrace.posterior.b2.values.flatten()
err = rTrace.posterior.eps.values.flatten()
aCI = np.percentile(aPost, [2.5, 97.5])
b1CI = np.percentile(b1Post,[2.5, 97.5])
b2CI = np.percentile(b2Post,[2.5, 97.5])
epsCI = np.percentile(err, [2.5, 97.5])

df = pd.read_pickle('SpikeN1P2.pkl')

df1 = df.loc[df.ISI==1.]
df1.reset_index(drop=True, inplace = True)

df5 = df.loc[df.ISI==5.]
df5.reset_index(drop=True, inplace = True)

df10 = df.loc[df.ISI==50.]
df10.reset_index(drop=True, inplace = True)

[nrows,ncols] = np.shape(df1)
spikeList = []
N1P2List = []
ISIList = []

for ck in range(nrows):

        curSPK = df1.spkRate[ck]
        spkMean = np.mean(curSPK)
        curSpont = df1.Spont[ck]
        sigSpont = 2*np.std(curSpont)
        if spkMean >sigSpont:
            spikeList.append(spkMean)
            curLFP = df1.N1P2[ck]
            N1P2Mean = np.mean(curLFP)*1000000
            N1P2List.append(N1P2Mean)
            #ePPList.append(ePP[ck])
            ISIList.append(float(df1.ISI[ck]))
spikeList = np.log(np.array(spikeList))
ISIList = np.array(ISIList)
spikeRange = np.arange(min(spikeList),np.max(spikeList))
#ISIList = np.log(ISIList)
plt.scatter(spikeList,N1P2List)

plt.plot(spikeRange,37+(2.2*spikeRange)+(-0.051*1)+11)
plt.plot(spikeRange,aCI[0]+(b1CI[0]*spikeRange)+(b2CI[0]*1)+epsCI[0])
plt.plot(spikeRange,aCI[1]+(b1CI[1]*spikeRange)+(b2CI[1]*1)+epsCI[1])
plt.show()

[nrows,ncols] = np.shape(df5)
spikeList = []
N1P2List = []
ISIList = []

for ck in range(nrows):

        curSPK = df5.spkRate[ck]
        spkMean = np.mean(curSPK)
        curSpont = df5.Spont[ck]
        sigSpont = 2*np.std(curSpont)
        if spkMean >sigSpont:
            spikeList.append(spkMean)
            curLFP = df5.N1P2[ck]
            N1P2Mean = np.mean(curLFP)*1000000
            N1P2List.append(N1P2Mean)
            #ePPList.append(ePP[ck])
            ISIList.append(float(df5.ISI[ck]))
spikeList = np.log(np.array(spikeList))
ISIList = np.array(ISIList)
spikeRange = np.arange(min(spikeList),np.max(spikeList))
#ISIList = np.log(ISIList)
plt.scatter(spikeList,N1P2List)

plt.plot(spikeRange,37+(2.2*spikeRange)+(-0.051*5)+11)
plt.plot(spikeRange,aCI[0]+(b1CI[0]*spikeRange)+(b2CI[0]*5)+epsCI[0])
plt.plot(spikeRange,aCI[1]+(b1CI[1]*spikeRange)+(b2CI[1]*5)+epsCI[1])
plt.show()

[nrows,ncols] = np.shape(df10)
spikeList = []
N1P2List = []
ISIList = []

for ck in range(nrows):

        curSPK = df10.spkRate[ck]
        spkMean = np.mean(curSPK)
        curSpont = df10.Spont[ck]
        sigSpont = 2*np.std(curSpont)
        if spkMean >sigSpont:
            spikeList.append(spkMean)
            curLFP = df10.N1P2[ck]
            N1P2Mean = np.mean(curLFP)*1000000
            N1P2List.append(N1P2Mean)
            #ePPList.append(ePP[ck])
            ISIList.append(float(df10.ISI[ck]))
spikeList = np.log(np.array(spikeList))
ISIList = np.array(ISIList)
spikeRange = np.arange(min(spikeList),np.max(spikeList))
#ISIList = np.log(ISIList)
plt.scatter(spikeList,N1P2List)

plt.plot(spikeRange,37+(2.2*spikeRange)+(-0.051*10)+11)
plt.plot(spikeRange,aCI[0]+(b1CI[0]*spikeRange)+(b2CI[0]*10)+epsCI[0])
plt.plot(spikeRange,aCI[1]+(b1CI[1]*spikeRange)+(b2CI[1]*10)+epsCI[1])
plt.show()

pdb.set_trace()