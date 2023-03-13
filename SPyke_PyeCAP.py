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
#Custom imports
from base.ts_data import _TsData              #Note this will change when packaged to .base, .io, etc.
from base.utils.base import _is_iterable

# pyeCAP io class imports
#from io.ripple_io import RippleIO, RippleArray
#from io.tdt_io import TdtIO, TdtArray, gather_sample_delay
import sys
sys.path.append('io')
from tdt_io import TdtIO, TdtArray, gather_sample_delay

# We will define the main class here.
class Spike(_TsData):
    """
    Purpose: This is the main spike analysis method. Within will hold analysis operations, data loaders, and plotters.
    Class Methods: 
        __init__: Initialize the class, load class variables
            Inputs: data - This is a string containing the name of the datafile to be analyzed
                    *args - Arguments to be passed to TsData parent class.
                    stores - Names of stores to load from TDT tank. If empty, load all stores
                    order - Set to True to order data sets by start time. Since data from the same file is read in chronological order,
                            this will only have an effect when reading in data from multiple files
                    rz_sample_rate : int sample rate of RZ processor in TDT chain
                    si_sample_rate : int sample rate of SI processor in TDT chain
        loadData: This loads data into memory. 
    """
    def __init__(self, data, *args, stores=None, order=True, rz_sample_rate=None, si_sample_rate=None, sample_delay=None,
                 **kwargs):
        self.exp_path = data
        # Work with file path
        if isinstance(data, str):
            file_path = data

            # Read in Ripple data files
            if file_path.endswith('.nev'):
                self.file_path = [file_path]
                self.io = [RippleIO(file_path)]
                data = RippleArray(self.io[0], type='ephys')
                chunks = data.chunks
                metadata = data.metadata
                daskify = True

            # Read in file types that point to a directory (i.e. tdt)
            elif os.path.isdir(file_path):
                # Check if directory is for tdt data
                tev_files = glob.glob(file_path + '/*.tev')  # There should only be one
                if len(tev_files) == 0:
                    # Check if this is a folder of tanks, look for tev files one live deep
                    tev_files = glob.glob(file_path + '/*/*.tev')
                    if len (tev_files) == 0:
                        raise FileNotFoundError("Could not located '*.tev' file expected for tdt tank.")
                    else:
                        data = [os.path.split(f)[0] for f in tev_files]
                        self.__init__(data, *args, stores=stores, rz_sample_rate=rz_sample_rate,
                                            si_sample_rate=si_sample_rate, sample_delay=sample_delay, **kwargs)
                        return
                elif len(tev_files) > 1:
                    raise FileExistsError("Multiple '*.tev' files found in tank, 1 expected.")
                else:
                    self.file_path = [file_path]
                    self.io = [TdtIO(file_path)]
                    data_store = TdtArray(self.io[0], type='ephys', stores=stores)
                    chunks = data_store.chunks
                    data = data_store.data
                    metadata = data_store.metadata
                    daskify = False
                    # set up sample delay to be ch_offsets parameter
                    if isinstance(sample_delay, list):
                        sample_delay = [-sd for sd in sample_delay]
                    elif sample_delay is not None:
                        sample_delay = [-int(sample_delay)] * len(metadata['ch_names'])

                    # add in delays from rz and si sample rate
                    if rz_sample_rate is not None or si_sample_rate is not None:
                        if sample_delay is None:
                            sample_delay = 0
                        # set tdt delays based on rz and si sample rates
                        rate_offsets = [-gather_sample_delay(rz_sample_rate, si_sample_rate)] * len(metadata['ch_names'])
                        sample_delay = np.add(sample_delay, rate_offsets )

            # File type not found
            else:
                if os.path.exists(file_path):
                    if os.path.isdir(file_path):
                        raise IOError('"' + file_path + '"  - is not a tdt tank.')
                    else:
                        _, file_extension = os.path.splitext(file_path)
                        raise IOError('"' + file_extension + '" is not a supported file extension')
                else:
                    raise IOError('"' + file_path + '"  - is not a file or directory.')

            super().__init__(data, metadata, *args, chunks=chunks, daskify=daskify, ch_offsets=sample_delay, **kwargs)

        # Work with iterable of file paths
        elif _is_iterable(data, str):
            self.file_path = data
            ephys_files = []
            for file in self.file_path:
                if isinstance(file, str):
                    ephys_data_set = type(self)(file, *args, stores=stores, rz_sample_rate=rz_sample_rate, si_sample_rate=si_sample_rate,
                                                sample_delay=sample_delay, **kwargs)
                    ephys_files.append(ephys_data_set)
                else:
                    raise IOError(
                        'Input is expected to be either a string containing a file path, or a list of file paths.')
            self.io = [item for d in ephys_files for item in d.io]
            data = [item for d in ephys_files for item in d.data]
            metadata = [item for d in ephys_files for item in d.metadata]
            chunks = [item for d in ephys_files for item in d.chunks]
            super().__init__(data, metadata, *args, chunks=chunks, daskify=False, order=order, **kwargs)

        else:
            super().__init__(data, *args, **kwargs)