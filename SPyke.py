#--------------------------------------------------------------------------------------------------------------------------------------------
# Authors: Brandon S Coventry            Wisconsin Institute for Translational Neuroengineering
# Date: 02/03/2023                       The night it was so cold, my car battery died at work... Wisconsin is cold
# Purpose: This is the header file for SPyke, a Python toolbox for analyzing Neural Spiking Data.
# Interface: At the moment, this uses TDT based reading and analysis, but can be extended to other systems.
# Revision History: Will be tracked in Github.
# Notes: N/A
#--------------------------------------------------------------------------------------------------------------------------------------------
# Imports go here. Global use imports will be put here, we will upload specifics as needed.
import numpy as np
import tdt              #For reading in tdt files
import matplotlib.pyplot as plt
import dask
import os
import glob
import sys
import pdb
import cupy as cp
from scipy.io import loadmat
from scipy.signal import sosfiltfilt
class Spike(object):
    """
    Purpose: This is the main spike analysis method. Within will hold analysis operations, data loaders, and plotters.
    Class Methods: 
        __init__: Initialize the class, load class variables
            Inputs: data - This is a string containing the name of the datafile to be analyzed
                    *args - Arguments to be passed to TsData parent class.
                    stores - Names of stores to load from TDT tank. If empty, load all stores. Stores should be in form of list i.e. ['EPOCHS','Streams']
                    rawDataStore - Names of raw data variable. Should point to 
                    rz_sample_rate : int sample rate of RZ processor in TDT chain
                    si_sample_rate : int sample rate of SI processor in TDT chain
        loadData: This loads data into memory. 
        TODO: Check if GPU flag is needed with cp.get_array_module
    """
    def __init__(self, data, stores=None, streamStore = None, rawDataStore=None, rz_sample_rate=None, si_sample_rate=None, sample_delay=None,GPU=True,stimulation=True,**kwargs):
        super().__init__()
        self.stores = stores
        if stores==None:
            self.data = tdt.read_block(data)
        else:
            self.data = tdt.read_block(data,'store',self.stores)
        print(self.data)
        self.GPU = GPU
        self.storage = getattr(self.data,streamStore)
        self.raw = getattr(self.storage,rawDataStore)
        self.rz_sample_rate = rz_sample_rate
        self.si_sample_rate = si_sample_rate
        self.sample_delay = sample_delay
        self.fs = self.raw['fs']
        #if self.GPU == True:
            #self.rawData = cp.asarray(self.raw['data'])            #Get this into a CuPy for GPU processing
        #else:
            #self.rawData = dask.delayed(self.raw['data'])          #Get this into a dask array for quick processing.
        self.rawData = self.raw['data']
        self.channel = self.raw['channel']
        
    
    def gpu2cpu(self,data2transfer):
        """
        This is a helper function to transfer gpu to cpu 
        Inputs: data2transfer - the data to move from GPU to CPU
        """
        return cp.asnumpy(data2transfer)
    
    def filterData(self,Type,channels=[]):
        """
        This function will filter the data for Spikes or for LFPs from predefined filters.
        Type - 'Spike' Will load a Chebychev type II filter with passband low = 500 and passband high = 5000
             - 'LFP' Will load a Chebychev type II filter with passband low = 3 and passband high = 500
        Channels - List of channels to filter. If empty, do all
        TODO - Independent channel filtering
        """
        if Type == 'Spike':
            SOSSpike = loadmat('SOS_Spike')
            SOS = np.ascontiguousarray(SOSSpike['SOS_Spike'])   #For reasons unknown to me, matlab saves SOS coeffs as non C-contiguous arrays. Fixed here
            filteredData = sosfiltfilt(SOS,self.rawData)
            self.SpikeFilterData = filteredData
        elif Type == 'LFP':
            SOSLFP = loadmat('SOS_LFP')
            SOS = np.ascontiguousarray(SOSLFP['SOS_LFP'])
            filteredData = sosfiltfilt(SOS,self.rawData)
            self.LFPFilterData = filteredData
        else:
            raise TypeError('Type must be "Spike" or "LFP"')
        return filteredData
    
    def extractStimEvents(self,window = [-10,20]):
        """
        This function reads in stimulation times, calculates the number of unique events, and extracts signals around those times with a window specified by window
        Inputs - Window - Times around which to grab data. Negative values indicate times 
        """
        self.stimTimes = self.data.scalars.semp.ts
        self.stimEvents = self.data.scalars.semp.data[0:3,:]
        [stimClasses,uWhere] = np.unique(self.stimEvents,return_index=True,axis=1)
        self.stimClass = np.sort(stimClasses,axis=0)
        nrowcol = np.shape(self.stimClass)
        self.numStims = nrowcol[1]
        #numRowsCols = np.shape(self.StimEvents)
        #self.numStims = numRowsCols[1]
        stimWhere = np.zeros(self.numStims,)
        for ck in range(self.numStims):
            curStim = self.StimClass[:,ck]
            stimWhere[ck,:] = np.where(self.stimEvents==curStim)
        self.stimWhere = stimWhere






        
        