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
class Spike(object):
    """
    Purpose: This is the main spike analysis method. Within will hold analysis operations, data loaders, and plotters.
    Class Methods: 
        __init__: Initialize the class, load class variables
            Inputs: data - This is a string containing the name of the datafile to be analyzed
                    *args - Arguments to be passed to TsData parent class.
                    stores - Names of stores to load from TDT tank. If empty, load all stores. Stores should be in form of list i.e. ['EPOCHS','Streams']
                    rz_sample_rate : int sample rate of RZ processor in TDT chain
                    si_sample_rate : int sample rate of SI processor in TDT chain
        loadData: This loads data into memory. 
    """
    def __init__(self, data, stores=None, rz_sample_rate=None, si_sample_rate=None, sample_delay=None,**kwargs):
        super().__init__()
        self.stores = stores
        if stores==None:
            self.data = tdt.read_block(data)
        else:
            self.data = tdt.read_block(data,'store',self.stores)
        print(self.data)
        self.rz_sample_rate = rz_sample_rate
        self.si_sample_rate = si_sample_rate
        self.sample_delay = sample_delay
        pdb.set_trace()
        
        