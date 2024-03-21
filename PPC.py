import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pdb
import arviz as az
import pymc as pm
import aesara
import matplotlib.pyplot as plt
import pdb
from mpl_toolkits.mplot3d import Axes3D
import json
import pickle # python3
import seaborn as sns

import jax
Prior5 = az.from_netcdf('ZMax_Prior5_HyperPrior5.netcdf')
Prior1 = az.from_netcdf('ZMax_Prior1_HyperPrior1.netcdf')
Prior0_5 = az.from_netcdf('ZMax_Prior0_5_HyperPrior0_5.netcdf')
Prior10 = az.from_netcdf('ZMax_Prior10_HyperPrior10.netcdf')
pdb.set_trace()
df_comp_loo = az.compare({"Prior 0.5": Prior0_5, "Prior 1": Prior1,"Prior 5": Prior5, "Prior 10": Prior10})
pdb.set_trace()