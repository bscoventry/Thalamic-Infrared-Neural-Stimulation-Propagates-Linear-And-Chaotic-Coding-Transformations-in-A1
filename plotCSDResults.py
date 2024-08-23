import numpy as np               #Numpy for numerical 'ala Matlab' computations
import matplotlib.pyplot as plt  #This works as our plotting tool
import pandas as pd              #Using pandas to read in CSV data files
import pickle                    #Pickle for saving data after completion of our model
import seaborn as sns            #We will use some of seaborn's distribution plotting tools
import pdb

data = pd.read_pickle("CSD_DF.pkl")      #Read in our data. Note this address may change based on where program files are downloaded.
Sinks = data.RMSSink                   #Let's consider young responses first.
Sources = data.RMSSource
Sinks = Sinks*1000
lepp = data.lepp
Sinks = np.log(Sinks+0.01)

a1MAP = -3.4
a2MAP = -0.86

a1CR = [-3.5,-3.2]
a2CR = [-.96,-0.75]

b1MAP = 0.049
b1CR = [0.023,0.078]
b2MAP = 0.066
b2CR = [0.036,0.098]

p1MAP = 0.25
p2MAP = 0.75
p1CR = [0.21,0.29]
p2CR = [0.71,0.79]

eppRange = np.arange(-6.90775528,1.5,0.01)
plt.figure(1)
plt.scatter(lepp,Sinks)
plt.plot(eppRange,a1MAP+b1MAP*eppRange,color='green')
plt.plot(eppRange,a1CR[0]+b1CR[1]*eppRange,'g--')
plt.plot(eppRange,a1CR[1]+b1CR[0]*eppRange,'g--')
plt.plot(eppRange,a2MAP+b2MAP*eppRange,color='blue')
plt.plot(eppRange,a2CR[0]+b2CR[1]*eppRange,'b--')
plt.plot(eppRange,a2CR[1]+b2CR[0]*eppRange,'b--')
plt.show()
