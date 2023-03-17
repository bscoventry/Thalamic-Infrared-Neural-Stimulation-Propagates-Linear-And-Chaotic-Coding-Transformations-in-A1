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
import pickle as pkl
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
    def __init__(self, data, stores=None, streamStore = None, rawDataStore=None,debug=0, rz_sample_rate=None, si_sample_rate=None, sample_delay=None,GPU=True,stimulation=True,SpksOrLFPs=['Spike','LFP'],**kwargs):
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
        self.numChannel = len(self.channel)
        self.totSamp = len(self.rawData[0,:])
        self.ts = np.arange(0,self.totSamp/self.fs,1/self.fs)
        if debug == 0:
            self.lineHarmonicFilter()
            if len(SpksOrLFPs) > 1:
                self.filterData('Spike')
                self.filterData('LFP')
            elif SpksOrLFPs == 'Spike':
                self.filterData('Spike')
            elif SpksOrLFPs == 'LFP':
                self.filterData('LFP')
            else:
                raise TypeError('SpkOrLFP flag must be "Spike","LFP", or ["Spike","LFP"]')
        elif debug == 1:
            print('Time to Debug!')
            with open('Spike.pkl','rb') as f:
                self.Spikes = pkl.load(f)
            f.close()
            with open('LFP.pkl','rb') as f:
                self.LFP = pkl.load(f)
            f.close()
        if 'Spike' in SpksOrLFPs:
            self.convertSpikes2Bin()
            self.sortSpikesKilosort()
        #self.extractStimEvents()
        
        
    
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
            filteredData = sosfiltfilt(SOS,self.lineFilterRawData)
            self.Spikes = filteredData
        elif Type == 'LFP':
            SOSLFP = loadmat('SOS_LFP')
            SOS = np.ascontiguousarray(SOSLFP['SOS_LFP'])
            filteredData = sosfiltfilt(SOS,self.lineFilterRawData)
            self.LFP = filteredData
        else:
            raise TypeError('Type must be "Spike" or "LFP"')
        return filteredData
        
    def lineHarmonicFilter(self):
       
        SOS60 = loadmat('SOS_60')
        SOS120 = loadmat('SOS_120')
        SOS240 = loadmat('SOS_240')
        SOS = np.ascontiguousarray(SOS60['SOS_60'])   #For reasons unknown to me, matlab saves SOS coeffs as non C-contiguous arrays. Fixed here
        filteredData1 = sosfiltfilt(SOS,self.rawData)
        SOS = np.ascontiguousarray(SOS120['SOS_120'])
        filteredData2 = sosfiltfilt(SOS,filteredData1)
        SOS = np.ascontiguousarray(SOS240['SOS_240'])
        filteredData3 = sosfiltfilt(SOS,filteredData2)
        self.lineFilterRawData = filteredData3
        
        return filteredData3
    
    def extractStimEvents(self,window = [-10,20]):
        """
        This function reads in stimulation times, calculates the number of unique events, and extracts signals around those times with a window specified by window
        Inputs - Window - Times around which to grab data. Negative values indicate times 
        TODO - Vectorize finding where each stim class falls during the recording period
        """
        self.stimTimes = self.data.scalars.semp.ts              #Get stim times from stores
        self.stimEvents = self.data.scalars.semp.data[0:3,:]    #We only need first 3 rows which carries stim period, num pulses, and pulse amplitude
        [stimClasses,uWhere] = np.unique(self.stimEvents,return_index=True,axis=1)        #Get the unique stim events. This might be 130Hz, -50ma, 30Hz, -70mA, etc.
        self.stimClass = np.sort(stimClasses,axis=0)                          #Order them just to make next data processing steps easier.
        nrowcol = np.shape(self.stimClass)                      #Helper variable to get the total number of stim classes
        self.numStims = nrowcol[1]
        #numRowsCols = np.shape(self.StimEvents)
        #self.numStims = numRowsCols[1]
        stimWhere = []
        for ck in range(self.numStims):                         #Hugely inefficient. Will vectorize. Till then, loop through the stim times and find where each stim class is.
            curStim = self.stimClass[:,ck]
            curStimRe = np.asarray([curStim[1],curStim[2],curStim[0]])
            idxStore = []
            for bc in range(len(self.stimTimes)):
                if np.array_equal(curStimRe,self.stimEvents[:,bc]):
                    idxStore.append(bc)
            stimWhere.append(idxStore)
            #stimWhere[ck,:] = np.where(self.stimEvents==curStim)
        self.stimWhere = stimWhere
        #Now get loop through and grab stim windows around the applied window
        try:
            windowSize = np.abs(window[0])+np.abs(window[1])
        except:
            raise ValueError('window should be a list or array of two values. window[0] = low time around which to grab data. window[1] = high time around which to grab data')
        windowSamples = len(np.arange(0,windowSize,1/self.fs))         #Again potentially silly way to do this, but works for now. Get the total number of samples needed per win
        [numStimClasses,self.numTrials] = np.shape(stimWhere)
        self.SpikeStore = dict()     #Convinient Storage! Yay!
        self.LFPStore = dict()
        for ck in range(numStimClasses):
            trialStoreArraySpikes = np.empty((self.numTrials,self.numChannel,windowSamples))
            trialStoreArrayLFPs = np.empty((self.numTrials,self.numChannel,windowSamples))
            trialStoreArraySpikes[:] = np.nan                               #Do Nans because we have to account for first stimulus that may be less than window size.
            trialStoreArrayLFPs[:] = np.nan
            storeKey = str(self.stimClass[0,ck])+'_'+str(self.stimClass[1,ck])+'_'+str(self.stimClass[2,ck])
            for bc in range(self.numTrials):
                curTimeIDX = self.stimWhere[ck][bc]
                curTime = self.stimTimes[curTimeIDX]
                if curTime+window[0] < 0:                  #Since this is shorter than winlow, we will add Nans to beginning of store file so that we are aligned with other trials
                    winLow = 0
                    winHighIDX = window[1]*self.fs
                    stimOn = np.where(self.ts == curTime)
                    if np.any(stimOn) == False:
                        diffTs = np.abs(self.ts-curTime)
                        whIDX = np.where(diffTs == min(diffTs))
                        stimOn = whIDX[0][0]
                    winHigh = round(np.asscalar(stimOn + winHighIDX))
                    shortDataSpikes = self.Spikes[:,winLow:winHigh]
                    shortDataLFP = self.LFP[:,winLow:winHigh]
                    [_,totSam] = np.shape(shortDataSpikes) 
                    numSamplesMissing = windowSamples-totSam
                    nanArraySpike = np.empty((self.numChannel,numSamplesMissing))
                    nanArraySpike[:] = np.nan
                    nanArrayLFP = np.empty((self.numChannel,numSamplesMissing))
                    nanArrayLFP[:] = np.nan
                    catArraySpike = np.empty((self.numChannel,windowSamples))
                    catArraySpike[:,0:numSamplesMissing] = nanArraySpike
                    catArraySpike[:,numSamplesMissing:numSamplesMissing+totSam] = shortDataSpikes
                    trialStoreArraySpikes[bc,:,:] = catArraySpike
                    catArrayLFP = np.empty((self.numChannel,windowSamples))
                    catArrayLFP[:,0:numSamplesMissing] = nanArrayLFP
                    catArrayLFP[:,numSamplesMissing:numSamplesMissing+totSam] = shortDataLFP
                    trialStoreArrayLFPs[bc,:,:] = catArrayLFP
                else:
                    stimOn = np.where(self.ts == curTime)
                    if np.any(stimOn) == False:         #Sometimes precision is off. Use this to find correct stim index if stimOn is empty
                        diffTs = np.abs(self.ts-curTime)
                        whIDX = np.where(diffTs == min(diffTs))
                        stimOn = whIDX[0][0]
                    winLowIDX = np.abs(window[0])*self.fs
                    winHighIDX = window[1]*self.fs
                    try:
                        winLow = round(np.asscalar(stimOn - winLowIDX))
                        winHigh = round(np.asscalar(stimOn + winHighIDX))
                    except:
                        print('well that was weird')
                        pdb.set_trace()
                    winHighDiff = windowSamples - len(range(winLow,winHigh))
                    
                    winHigh = winHigh + winHighDiff           #Make sure arrays are same shape
                    trialStoreArraySpikes[bc,:,:] = self.Spikes[:,winLow:winHigh]          #Store all trials, all electrodes, windows into arrays that will be loaded into a dictionary
                    trialStoreArrayLFPs[bc,:,:] = self.LFP[:,winLow:winHigh]
            self.SpikeStore[storeKey] = trialStoreArraySpikes
            self.LFPStore[storeKey] = trialStoreArrayLFPs
    
    def sortSpikesKilosort(self,matlabKilosortPath = 'C://Users//coventry//CodeRepos//Kilosort-main//Kilosort-main'):
        """
        This function will create a call to matlab to run units for spike sorting. Note requires matlab python plugin to run.
        Reguires a compiled version of kilosort to work. Operates by opening gui for visualization of traces
        """
        import matlab.engine               #Get a hold of matlab
        eng = matlab.engine.start_matlab() #Start Matlab
        ksortPath = eng.genpath(r'C://Users//coventry//CodeRepos//Kilosort-main//Kilosort-main')    #Need to tell python where kilosort is
        eng.addpath(ksortPath,nargout=0)
        eng.kilosort()                  #Run kilosort
    
    def convertSpikes2Bin(self,scaleFactor=1e6,binName = 'SpikeKilosort.bin'):
        """
        This function converts Spike data into a .bin file for kilosort
        Inputs - scaleFactor: Data is typically float like, but kilosort needs int16. To get the resolution needed for uV, 
        need to scale data by this factor so that every data point is not immediately cast to 0 from conversion from float to int 16.
        This varies based on recording setup, electrodes. For example, TDT recommends 1e6 conversion for their systems and converts to
        microvolts.
        Bin file is a matrix of shape [nelectrodes x ntimepoints]. Our class varialbe Spike is already in this form.
        """
        try:
            data = (self.Spikes)*scaleFactor
        except:
            raise RuntimeError('Spikes not found in class. Can only run this conversion if Spikes are available')
        with open(binName, 'wb') as fh:
            pkl.dump(data, fh)
    
    def plotSampleWaveform(self,data,channel,time2Plot=[]):
        """
        This is a sample helper function just to plot some data.
        """
        for ck in range(len(channel)):
            plt.figure(ck)
            if bool(time2Plot)==False:
                plt.plot(self.ts,data[channel[ck],:])
            else:
                plt.plot(self.ts[time2Plot],data[channel[ck],time2Plot])
        
        


                    

                









        
        