#----------------------------------------------------------------------------------------------------------------------------------
# Author: Brandon S Coventry PhD
# Date: 03/18/24
# Purpose: COG Analyses
# Revision History: See github
#----------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pdb

COG = pd.read_pickle('LFPCOG.pkl')
pdb.set_trace()
instV = COG.maxInstVel
epp = COG.EnergyPerPulse
dist = COG.distance
waveTime = COG.waveTime
 #Create a distribution plot of the data.
sns.scatterplot(x=epp, y=dist)
plt.show()