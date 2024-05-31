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
df = pd.read_pickle('sampleCSD.pkl')
#[numrows,numcols] = np.shape(df)
numrows = 1
EPP = df['EnergyPerPulse']
ISI = df['ISI']
xarray = df['xarray']
yarray = df['yarray']
pdb.set_trace()
for ck in range(numrows):
    curCSD = df['estCSD']#[ck]
    maxCurrentSink = np.empty((1526,))
    maxCurrentSource = np.empty((1526,))
    for bc in range(1526):
        curcurCSD = curCSD[:,:,bc]
        maxCurrentSink[bc] = np.min(curcurCSD)
        maxCurrentSource[bc] = np.max(curcurCSD)
    maxSinkWhere = np.where(curCSD==maxCurrentSink)
    maxSourceWhere = np.where(curCSD==maxCurrentSource)
    