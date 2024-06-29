import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pdb
import seaborn as sns
df = pd.read_pickle('LFPBandChange.pkl')
epp = df['EnergyPerPulse'].values
ISI = df['ISI'].values
beta = df['betaDiff'].values
hg = df['hgDiff']
lepp = np.log(epp+0.015)
lISI = np.log(ISI+0.015)

ener = np.linspace(-7,1.5,num=1000)
iList = np.linspace(-2.2,4.6,num=1000)
betaBSlope = 0.17
betaBInter = 0.58
betaBISI = -0.017
betaBInteraction = -0.016
betaBError = 0.89

betaBSlopeCI = [0.091,0.25]
betaBInterCI = [0.37, 0.8]
betaBISICI = [-0.08,0.015]
betaBInteractionCI = [-0.024,-0.0059] 
betaBErrorCI = [0.8,1]

MAP = betaBInter + (ener*betaBSlope) + (iList*betaBISI) + (ener*iList*betaBInteraction) + betaBError
MAPCI_L = betaBInterCI[0] + (ener*betaBSlopeCI[0]) + (iList*betaBISICI[0]) + (ener*iList*betaBInteractionCI[0]) + betaBErrorCI[0]
MAPCI_H = betaBInterCI[1] + (ener*betaBSlopeCI[1]) + (iList*betaBISICI[1]) + (ener*iList*betaBInteractionCI[1]) + betaBErrorCI[1]

plt.scatter(lepp,beta)
plt.plot(ener,MAP,'g')
plt.plot(ener,MAPCI_L,'r')
plt.plot(ener,MAPCI_H,'r')
plt.title('Beta Band')
plt.show()


betaHGSlope = 0.49
betaHGInter = 2
betaHGISI = -0.055
betaHGInteraction = -0.036
betaHGError = 1.5

betaHGSlopeCI = [0.31,0.67]
betaHGInterCI = [1.5, 2.4]
betaHGISICI = [-0.19,0.079]
betaHGInteractionCI = [-0.092,0.0094] 
betaHGErrorCI = [1.4,1.7]

MAPHG = betaHGInter + (ener*betaHGSlope) + (iList*betaHGISI) + (ener*iList*betaHGInteraction) + betaHGError
MAPCI_LHG = betaHGInterCI[0] + (ener*betaHGSlopeCI[0]) + (iList*betaHGISICI[0]) + (ener*iList*betaHGInteractionCI[0]) + betaHGErrorCI[0]
MAPCI_HHG = betaHGInterCI[1] + (ener*betaHGSlopeCI[1]) + (iList*betaHGISICI[1]) + (ener*iList*betaHGInteractionCI[1]) + betaHGErrorCI[1]

plt.scatter(lepp,hg)
plt.plot(ener,MAPHG,'g')
plt.plot(ener,MAPCI_LHG,'r')
plt.plot(ener,MAPCI_HHG,'r')
plt.title('High Gamma Band')
plt.show()

betaLGSlope = 0.34
betaLGInter = 1
betaLGISI = 0.024
betaLGInteraction = -0.0018
betaLGError = 1.5

betaLGSlopeCI = [0.21,0.47]
betaLGInterCI = [0.73, 1.4]
betaLGISICI = [-0.061,0.093]
betaLGInteractionCI = [-0.019,0.014] 
betaLGErrorCI = [1.3,1.7]

MAPLG = betaLGInter + (ener*betaLGSlope) + (iList*betaLGISI) + (ener*iList*betaLGInteraction) + betaLGError
MAPCI_LLG = betaLGInterCI[0] + (ener*betaLGSlopeCI[0]) + (iList*betaLGISICI[0]) + (ener*iList*betaLGInteractionCI[0]) + betaLGErrorCI[0]
MAPCI_HLG = betaLGInterCI[1] + (ener*betaLGSlopeCI[1]) + (iList*betaLGISICI[1]) + (ener*iList*betaLGInteractionCI[1]) + betaLGErrorCI[1]

plt.scatter(lepp,hg)
plt.plot(ener,MAPLG,'g')
plt.plot(ener,MAPCI_LLG,'r')
plt.plot(ener,MAPCI_HLG,'r')
plt.title('Low Gamma Band')
plt.show()
pdb.set_trace()