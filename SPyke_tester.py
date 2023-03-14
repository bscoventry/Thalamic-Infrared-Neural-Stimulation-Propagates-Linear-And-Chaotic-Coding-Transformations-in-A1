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
from SPyke import Spike
import pdb
dataPath = 'C://Users//coventry//DataRepos//R144-220829-160841'
stores = None             #Load all stores
streamStore = 'streams'
rawDataStore = 'TDT2'
SpikeClass = Spike(dataPath,stores,streamStore,rawDataStore)
Type = 'Spike'
pdb.set_trace()
#filterData = SpikeClass.filterData(Type)
SpikeClass.extractStimEvents()
