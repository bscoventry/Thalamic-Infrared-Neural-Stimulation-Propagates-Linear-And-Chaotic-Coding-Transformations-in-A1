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

df = pd.read_pickle('sampleCSD.pkl')
#[numrows,numcols] = np.shape(df)
numrows = 1
EPP = df['EnergyPerPulse']
ISI = df['ISI']
pdb.set_trace()
for ck in range(numrows):
    curCSD = df['estCSD']#[ck]