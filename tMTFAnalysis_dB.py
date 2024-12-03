import numpy as np
import scipy.io as sio
import pandas as pd
import pdb
import matplotlib.pyplot as plt

df = pd.read_pickle('LFP_tMTF_long_dB.pkl')

nRows = len(df)
mTMTFm = np.zeros((nRows,))
#mTMTFs = np.zeros((nRows,))
#for ck in range(nRows):
    #curtMTF = df.tMFT[ck]
    #curtMTFs = df.tMTFS[ck]
    #mTMTFm[ck] = 10*np.log10(np.max(curtMTF)/curtMTF[0])

#df["mTMTFm"] = mTMTFm
uniqueFreq = np.unique(df.fundFreq)
#uniqueFreq = np.delete(uniqueFreq,-1)
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
    elif curE > 3.5: #and curE <= 4:
        index = 7
    #elif curE > 4:
        #index = 8
    histLoc[ck] = index
df["histLoc"] = histLoc

getVals = df.tMTF.values#np.concatenate(df.tMTF.values)
ymin = np.min(getVals)
ymax = np.max(getVals)
# for ck in range(len(uniqueFreq)):
#     curFreq = uniqueFreq[ck]
#     curDF = df.loc[df['fundFreq'] == curFreq]
#     curDF.reset_index(drop=True, inplace = True)
    
#     curDF.boxplot(column = 'tMTF',by='histLoc')
#     plt.ylim(ymin, ymax)
#     plt.title(str(curFreq))
#     plt.show()
perValues = np.zeros((8,5))
perValuesNeg = np.zeros((8,5))
for bc in range(8):
    newDF = df.loc[df['histLoc'] == bc]
    newDF.reset_index(drop=True, inplace = True)
    newDF.boxplot(column = 'tMTF',by='fundFreq')
    plt.axhline(y = 3, color = 'r', linestyle = '-') 
    plt.axhline(y = -3, color = 'r', linestyle = '-') 
    if bc == 0:
        plt.title('0-0.5 mJPP')
    if bc == 1:
        plt.title('0.5-1 mJPP')
    if bc == 2:
        plt.title('1-1.5 mJPP')
    if bc == 3:
        plt.title('1.5-2 mJPP')
    if bc == 4:
        plt.title('2-2.5 mJPP')
    if bc == 5:
        plt.title('2.5-3 mJPP')
    if bc == 6:
        plt.title('3-3.5 mJPP')
    if bc == 7:
        plt.title('>3.5 mJPP')
    numISIs = np.unique(newDF.fundFreq.values)
    if len(numISIs) > 5:
        numISIs = np.delete(numISIs,3)
    print(numISIs)
    plt.ylim(ymin, ymax)
    for jk in range(len(numISIs)):
        newnewDF = newDF.loc[newDF['fundFreq']==numISIs[jk]]
        newnewDF.reset_index(drop=True,inplace=True)
        curV = newnewDF.tMTF.values
        sigWhere = np.where(curV>=3)
        sigWhereNeg = np.where(curV<=-3)
        perSigWhere = (len(sigWhere[0])/len(curV))*100
        perSigWhereNeg = (len(sigWhereNeg[0])/len(curV))*100
        perValues[bc,jk] = perSigWhere
        perValuesNeg[bc,jk] = perSigWhereNeg
print('Increase')
for jvk in range(8):
    print(perValues[jvk,:])
print('Decrease')
for jvk in range(8):
    print(perValuesNeg[jvk,:])
plt.show()