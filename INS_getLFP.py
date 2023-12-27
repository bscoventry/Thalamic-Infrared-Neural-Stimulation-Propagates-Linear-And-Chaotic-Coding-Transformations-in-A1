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
from SPyke import Spike_Processed
import pdb
import scipy.io as sio
if __name__ == "__main__":
    dataStore = {}
    
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200821'
    PU = 5
    PW = 0.2
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_21_20//INS_5PU_0_2PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200821'
    PU = 5
    PW = 0.2
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_21_20//INS_5PU_0_2PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200821'
    PU = 5
    PW = 0.5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_21_20//INS_5PU_0_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200821'
    PU = 5
    PW = 0.5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_21_20//INS_5PU_0_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200821'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_21_20//INS_5PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200821'
    PU = 5
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_21_20//INS_5PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200821'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_21_20//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200824'
    PU = 5
    PW = 0.1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_24_20//INS_5PU_0_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200824'
    PU = 5
    PW = 0.2
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_24_20//INS_5PU_0_2PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200824'
    PU = 5
    PW = 0.5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_24_20//INS_5PU_0_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200824'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_24_20//INS_5PU_1PW_5ISI_2' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200824'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_24_20//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 0.2
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_26_20//INS_5PU_0_2PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 0.2
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_26_20//INS_5PU_0_2PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 0.5
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_26_20//INS_5PU_0_5PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 0.5
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_26_20//INS_5PU_0_5PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 1
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_26_20//INS_5PU_1PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 1
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_26_20//INS_5PU_1PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 5
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_26_20//INS_5PU_5PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 5
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_26_20//INS_5PU_5PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200831'
    PU = 5
    PW = 0.2
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_31_20//INS_5PU_0_2PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200831'
    PU = 5
    PW = 0.5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_31_20//INS_5PU_0_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200831'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_31_20//INS_5PU_1PW_5ISI_2' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200831'
    PU = 5
    PW = 1
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_31_20//INS_5PU_1PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200831'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_31_20//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200831'
    PU = 5
    PW = 5
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_31_20//INS_5PU_5PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200831'
    PU = 5
    PW = 10
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//08_31_20//INS_5PU_10PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200902'
    PU = 5
    PW = 0.5
    ISI = 20
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_02_20//INS_5PU_0_5PW_20ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200902'
    PU = 5
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_02_20//INS_5PU_1PW_1ISI_3' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200902'
    PU = 5
    PW = 5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_02_20//INS_5PU_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200902'
    PU = 5
    PW = 5
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_02_20//INS_5PU_5PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200902'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_02_20//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200902'
    PU = 5
    PW = 10
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_02_20//INS_5PU_10PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200903'
    PU = 5
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_03_20//INS_5PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200903'
    PU = 5
    PW = 0.1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_03_20//INS_5PU_0_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200903'
    PU = 5
    PW = 0.2
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_03_20//INS_5PU_0_2PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200903'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_03_20//INS_5PU_10PW_50ISI_3' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200909'
    PU = 5
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_09_20//INS_5PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200909'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_09_20//INS_5PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200909'
    PU = 5
    PW = 1
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_09_20//INS_5PU_1PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2007'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200909'
    PU = 5
    PW = 1
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2007//09_09_20//INS_5PU_1PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore
    try:
        sio.savemat('LFP.mat',dataStore)
    except:
        print('Matlab data did not save')
        pdb.set_trace()

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200822'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_22_20//INS_5PU_1PW_5ISI_2' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200822'
    PU = 5
    PW = 0.2
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_22_20//INS_5PU_0_2PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200822'
    PU = 5
    PW = 0.5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_22_20//INS_5PU_0_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200822'
    PU = 5
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_22_20//INS_5PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200822'
    PU = 5
    PW = 5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_22_20//INS_5PU_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200822'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_22_20//INS_5PU_5PW_5ISI_2' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200825'
    PU = 5
    PW = 5
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_25_20//INS_5PU_5PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200825'
    PU = 5
    PW = 0.2
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_25_20//INS_5PU_0_2PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200825'
    PU = 5
    PW = 0.5
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_25_20//INS_5PU_0_5PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200825'
    PU = 5
    PW = 1
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_25_20//INS_5PU_1ms_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_26_20_2//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 0.2
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_26_20_2//INS_5PU_0_2PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 0.2
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_26_20_2//INS_5PU_0_2PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 0.5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_26_20_2//INS_5PU_0_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 0.5
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_26_20_2//INS_5PU_0_5PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_26_20_2//INS_5PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 1
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_26_20_2//INS_5PU_1PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200826'
    PU = 5
    PW = 5
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//08_26_20_2//INS_5PU_5PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200901'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_01_20//INS_5PU_5PW_5ISI_2' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200901'
    PU = 5
    PW = 0.2
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_01_20//INS_5PU_0_2PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200901'
    PU = 5
    PW = 0.5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_01_20//INS_5PU_0_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200901'
    PU = 5
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_01_20//INS_5PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200901'
    PU = 5
    PW = 5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_01_20//INS_5PU_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200901'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_01_20//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200908'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_08_20//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200908'
    PU = 5
    PW = 0.1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_08_20//INS_5PU_0_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200908'
    PU = 5
    PW = 0.2
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_08_20//INS_5PU_0_2PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200908'
    PU = 5
    PW = 0.5
    ISI = 20
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_08_20//INS_5PU_0_5PW_20ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200908'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_08_20//INS_5PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200908'
    PU = 5
    PW = 1
    ISI = 20
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_08_20//INS_5PU_1PW_20ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2008'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20200908'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2008//09_08_20//INS_5PU_10PW_50ISI_3' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    try:
        sio.savemat('LFP.mat',dataStore)
    except:
        print('Matlab data did not save')
        pdb.set_trace()

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201031'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//10_31_20//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201031'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//10_31_20//INS_5PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201031'
    PU = 5
    PW = 5
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//10_31_20//INS_5PU_5PW_100ISI_LaserOn' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201031'
    PU = 5
    PW = 0.5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//10_31_20//INS_5PU_0_5ms_5ISI_2' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201101'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_01_20//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201101'
    PU = 5
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_01_20//INS_5PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201101'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_01_20//INS_5PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201101'
    PU = 5
    PW = 5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_01_20//INS_5PU_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201101'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_01_20//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201102'
    PU = 5
    PW = 5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_02_20//INS_5PU_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201102'
    PU = 5
    PW = 0.5
    ISI = 0.3
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_02_20//INS_5PU_0_5PW_0_3ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201102'
    PU = 5
    PW = 0.5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_02_20//INS_5PU_0_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201102'
    PU = 5
    PW = 10
    ISI = 25
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_02_20//INS_5PU_10PW_25ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201102'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_02_20//INS_5PU_10PW_50ISI_2' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201102'
    PU = 10
    PW = 0.5
    ISI = 0.25
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_02_20//INS_10PU_0_5PW_0_25ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201104'
    PU = 1
    PW = 5
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_04_20//INS_1PU_5PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201104'
    PU = 1
    PW = 0.2
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_04_20//INS_1PU_0_2PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201104'
    PU = 1
    PW = 0.5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_04_20//INS_1PU_0_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201104'
    PU = 1
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_04_20//INS_1PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201104'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_04_20//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201104'
    PU = 10
    PW = 0.2
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_04_20//INS_10PU_0_2PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201107'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_07_20//INS_5PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

     #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201107'
    PU = 5
    PW = 0.2
    ISI = 0.2
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_07_20//INS_5PU_0_2PW_0_2ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

     #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201107'
    PU = 5
    PW = 0.5
    ISI = 0.5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_07_20//INS_5PU_0_5PW_0_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

     #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201107'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_07_20//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

     #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201107'
    PU = 10
    PW = 1
    ISI =1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_07_20//INS_10PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201109'
    PU = 5
    PW = 1
    ISI = 0.5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_09_20//INS_5PU_1PW_0_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201109'
    PU = 5
    PW = 0.2
    ISI = 0.5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_09_20//INS_5PU_0_2PW_0_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201109'
    PU = 5
    PW = 0.5
    ISI = 0.5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_09_20//INS_5PU_0_5PW_0_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201109'
    PU = 10
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_09_20//INS_10PU_1PW_1ISI_2' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201110'
    PU = 1
    PW = 5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_10_20//INS_1PU_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201110'
    PU = 1
    PW = 0.2
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_10_20//INS_1PU_0_2PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201110'
    PU = 1
    PW = 0.5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_10_20//INS_1PU_0_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201110'
    PU = 1
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_10_20//INS_1PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201110'
    PU = 1
    PW = 10
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_10_20//INS_1PU_10PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201112'
    PU = 10
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_12_20//INS_10PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201112'
    PU = 10
    PW = 0.2
    ISI = 0.5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_12_20//INS_10PU_0_2PW_0_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201112'
    PU = 10
    PW = 0.5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_12_20//INS_10PU_0_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201112'
    PU = 10
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_12_20//INS_10PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201112'
    PU = 10
    PW = 10
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_12_20//INS_10PU_10PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201129'
    PU = 5
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_29_20//INS_5PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201129'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_29_20//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201129'
    PU = 5
    PW = 10
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_29_20//INS_5PU_10PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201129'
    PU = 5
    PW = 10
    ISI = 25
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_29_20//INS_5PU_10PW_25ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2013'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201129'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2013//11_29_20//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore



    try:
        sio.savemat('LFP.mat',dataStore)
    except:
        print('Matlab data did not save')
        pdb.set_trace()

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201126'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_26_20//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201126'
    PU = 1
    PW = 10
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_26_20//INS_1PU_10PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201126'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_26_20//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201126'
    PU = 10
    PW = 0.5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_26_20//INS_10PU_0_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201126'
    PU = 10
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_26_20//INS_10PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201126'
    PU = 10
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_26_20//INS_10PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201128'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_28_20//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201128'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_28_20//INS_5PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201128'
    PU = 5
    PW = 10
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_28_20//INS_5PU_10PW_5PW' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201128'
    PU = 5
    PW = 10
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_28_20//INS_5PU_10PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201128'
    PU = 5
    PW = 10
    ISI = 25
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_28_20//INS_5PU_10PW_25ISI_2' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201128'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_28_20//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201130'
    PU = 1
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_30_20//INS_1PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201130'
    PU = 1
    PW = 0.2
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_30_20//INS_1PU_0_2PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201130'
    PU = 1
    PW = 0.5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_30_20//INS_1PU_0_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201130'
    PU = 1
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_30_20//INS_1PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201130'
    PU = 1
    PW = 10
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_30_20//INS_1PU_10PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201130'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//11_30_20//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201202'
    PU = 5
    PW = 5
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_02_20//INS_5PU_5PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201202'
    PU = 5
    PW = 0.1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_02_20//INS_5PU_0_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201202'
    PU = 5
    PW = 0.1
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_02_20//INS_5PU_0_1PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201202'
    PU = 5
    PW = 0.2
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_02_20//INS_5PU_0_2PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201202'
    PU = 5
    PW = 0.5
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_02_20//INS_5PU_0_5PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201202'
    PU = 5
    PW = 0.8
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_02_20//INS_5PU_0_8PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201202'
    PU = 5
    PW = 1
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_02_20//INS_5PU_1PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201202'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_02_20//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201203'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_03_20//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201203'
    PU = 5
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_03_20//INS_5PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201203'
    PU = 5
    PW = 1
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_03_20//INS_5PU_1PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201203'
    PU = 5
    PW = 5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_03_20//INS_5PU_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201203'
    PU = 5
    PW = 5
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_03_20//INS_5PU_5PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201203'
    PU = 5
    PW = 10
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_03_20//INS_5PU_10PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201203'
    PU = 5
    PW = 10
    ISI = 10
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_03_20//INS_5PU_10PW_10ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201214'
    PU = 5
    PW = 5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_14_20//INS_5PU_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201214'
    PU = 5
    PW = 0.5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_14_20//INS_5PU_0_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201214'
    PU = 5
    PW = 10
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_14_20//INS_5PU_10PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2015'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20201214'
    PU = 5
    PW = 10
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2015//12_14_20//INS_5PU_10PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    
    try:
        sio.savemat('LFP.mat',dataStore)
    except:
        print('Matlab data did not save')
        pdb.set_trace()

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210215'
    PU = 5
    PW = 0.2
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_15_21//INS_5PU_0_2PW_1ISI_5' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210215'
    PU = 5
    PW = 0.5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_15_21//INS_5PU_0_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210215'
    PU = 5
    PW = 10
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_15_21//INS_5PU_10PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210216'
    PU = 5
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_16_21//INS_5PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210216'
    PU = 5
    PW = 0.2
    ISI = 0.1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_16_21//INS_5PU_0_2PW_0_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210216'
    PU = 5
    PW = 0.5
    ISI = 0.2
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_16_21//INS_5PU_0_5PW_0_2ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210216'
    PU = 5
    PW = 0.7
    ISI = 0.5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_16_21//INS_5PU_0_7PW_0_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210216'
    PU = 5
    PW = 1
    ISI = 0.5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_16_21//INS_5PU_1PW_0_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210216'
    PU = 5
    PW = 5
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_16_21//INS_5PU_5PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210216'
    PU = 5
    PW = 10
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_16_21//INS_5PU_10PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210219'
    PU = 5
    PW = 10
    ISI = 100
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_19_21//INS_5PU_10PW_100ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210219'
    PU = 50
    PW = 0.5
    ISI = 0.2
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_19_21//INS_50PU_0_5PW_0_2ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210222'
    PU = 10
    PW = 5
    ISI = 5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_22_21//INS_10PU_5PW_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210222'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_22_21//INS_5PU_10PW_50ISI_2' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210222'
    PU = 10
    PW = 0.2
    ISI = 0.5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_22_21//INS_10PU_0_2PW_0_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210222'
    PU = 10
    PW = 0.2
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_22_21//INS_10PU_0_2PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210222'
    PU = 10
    PW = 0.5
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_22_21//INS_10PU_0_5PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210222'
    PU = 10
    PW = 1
    ISI = 1
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_22_21//INS_10PU_1PW_1ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210222'
    PU = 20
    PW = 0.2
    ISI = 0.5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_22_21//INS_20PU_0_2PW_0_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210225'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_25_21//INS_5PU_10PW_50ISI_4' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210225'
    PU = 5
    PW = 0.7
    ISI = 0.5
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_25_21//INS_5PU_0_7PW_0_5ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    #
    animalName = 'INS2102'
    if animalName == 'INS2013':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2007':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431])
    elif animalName == 'INS2015':
        power = np.array([-1.1, 62.1, 77.42, 87.4, 101.2, 115.9, 130, 184.34, 257.3, 308.8, 360.7, 374.4])
    elif animalName == 'INS2102':
        power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    elif animalName == 'INS2008':
        power = np.array([0, 4, 117, 130, 143.17, 155.9, 207, 292, 357, 370, 410, 431]) 
    else:
        print('Brandon you messed')
        pdb.set_trace()
           
    Date = '20210226'
    PU = 5
    PW = 10
    ISI = 50
    storage = animalName+'_'+Date+'_'+str(PU)+'_'+str(PW)+'_'+str(ISI)
    dataPath = 'Z://PhDData//INSdata//INS2102//02_26_21//INS_5PU_10PW_50ISI' #'C://Users//coventry//Desktop//P119-230317-165356'
    #power = np.array([-1.4, 37.2, 46.15, 58.6, 88, 94, 123, 182.62, 259, 313.6, 386.1, 414])
    stores = None             #Load all stores
    streamStore = 'streams'
    debug = 0
    stim = 0
    Type = 'LFP'
    SpksOrLFPs = [Type]
    try:
        SpikeClass = Spike_Processed(dataPath,PU,PW,ISI,power,stores,streamStore,debug,stim,SpksOrLFPs=SpksOrLFPs)
    except:
        print('File'+dataPath+'Did not Work')

    #Spikes = SpikeClass.Spikes
    LFPs = SpikeClass.LFP
    #SpikeClass.plotSampleWaveform(Spikes,[1])
    #SpikeClass.plotSampleWaveform(LFPs,[1])
    #Sxx,t,f = SpikeClass.getLFPSpectrogram([0])
    alpha = SpikeClass.epocedAlpha
    beta = SpikeClass.epochedBeta
    theta = SpikeClass.epochedTheta
    lowGamma = SpikeClass.epochedLowGamma
    highGamma = SpikeClass.epochedHighGamma
    
    
    bandStore={}
    bandStore['alpha'] = alpha 
    bandStore['beta'] = beta
    bandStore['theta'] = theta
    bandStore['lowgamma'] = lowGamma
    bandStore['highgamma'] = highGamma    
    dataStore[storage]=bandStore

    try:
        sio.savemat('LFP.mat',dataStore)
    except:
        print('Matlab data did not save')
        pdb.set_trace()

    print('Done!')
    pdb.set_trace()
    #filterData = SpikeClass.filterData(Type)
    #SpikeClass.stimArtifactRemoval(algo='Template')

