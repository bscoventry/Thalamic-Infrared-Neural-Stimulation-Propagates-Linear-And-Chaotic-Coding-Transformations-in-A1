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
# We will define the main class here.
class Spike(object):
    """
    Purpose: This is the main spike analysis method. Within will hold analysis operations, data loaders, and plotters.
    Class Methods: 
        __init__: Initialize the class, load class variables
            Inputs: dataObject - This is a string containing the name of the datafile to be analyzed
                    dataLoader - This is a string containing the name of the format of the data. Right now, only 'tdt' is recognized
        loadData: This loads data into memory. 
    """
    def __init__(self,dataObject,dataLoader):
        super(Spike, self).__init__()
        self.dataObject = dataObject
        self.dataLoader = dataLoader
        self.data = []
    def loadData(self):
        if self.dataLoader == 'tdt':
            self.data = tdt.read_block(self.dataObject)
        else:
            raise TypeError("Only 'tdt' option available currently.")