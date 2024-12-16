import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pdb
import seaborn as sns
df = pd.read_pickle('LFPBandChangeLong.pkl')
epp = df['EnergyPerPulse'].values
ISI = df['ISI'].values
beta = df['betaDiff'].values
hg = df['hgDiff']
lg = df['lgDiff']
lepp = np.log(epp+0.015)
lISI = np.log(ISI+0.015)

ener = np.linspace(-7,1.5,num=1000)
iList = np.linspace(-2.2,4.6,num=1000)
betaBSlope = -0.14
betaBInter = -0.23
betaBISI = -0.03
betaBInteraction = -0.0074
betaBError = 1.4

betaBSlopeCI = [-0.25,-0.033]
betaBInterCI = [-0.51, 0.036]
betaBISICI = [-0.092,0.034]
betaBInteractionCI = [-0.02,0.01] 
betaBErrorCI = [1.2,1.5]

MAP = betaBInter + (ener*betaBSlope) + (iList*betaBISI) + (ener*iList*betaBInteraction) + betaBError
MAPCI_L = betaBInterCI[0] + (ener*betaBSlopeCI[0]) + (iList*betaBISICI[0]) + (ener*iList*betaBInteractionCI[0]) + betaBErrorCI[0]
MAPCI_H = betaBInterCI[1] + (ener*betaBSlopeCI[1]) + (iList*betaBISICI[1]) + (ener*iList*betaBInteractionCI[1]) + betaBErrorCI[1]

plt.scatter(lepp,beta)
plt.plot(ener,MAP,'g')
plt.plot(ener,MAPCI_L,'r')
plt.plot(ener,MAPCI_H,'r')
plt.title('Beta Band')
plt.show()


betaHGSlope = -0.1
betaHGInter = 0.66
betaHGISI = -0.059
betaHGInteraction = 0.0027
betaHGError = 2.1

betaHGSlopeCI = [-0.22,0.0041]
betaHGInterCI = [0.35, 0.97]
betaHGISICI = [-0.14,0.02]
betaHGInteractionCI = [-0.018,0.028] 
betaHGErrorCI = [1.8,2.3]

MAPHG = betaHGInter + (ener*betaHGSlope) + (iList*betaHGISI) + (ener*iList*betaHGInteraction) + betaHGError
MAPCI_LHG = betaHGInterCI[0] + (ener*betaHGSlopeCI[0]) + (iList*betaHGISICI[0]) + (ener*iList*betaHGInteractionCI[0]) + betaHGErrorCI[0]
MAPCI_HHG = betaHGInterCI[1] + (ener*betaHGSlopeCI[1]) + (iList*betaHGISICI[1]) + (ener*iList*betaHGInteractionCI[1]) + betaHGErrorCI[1]

plt.scatter(lepp,hg)
plt.plot(ener,MAPHG,'g')
plt.plot(ener,MAPCI_LHG,'r')
plt.plot(ener,MAPCI_HHG,'r')
plt.title('High Gamma Band')
plt.show()

betaLGSlope = -0.24
betaLGInter = -0.078
betaLGISI = -0.037
betaLGInteraction = 0.0034
betaLGError = 2.1

betaLGSlopeCI = [-0.39,-0.096]
betaLGInterCI = [-0.46, 0.3]
betaLGISICI = [-0.1,0.033]
betaLGInteractionCI = [-0.024,0.046] 
betaLGErrorCI = [1.9,2.3]

MAPLG = betaLGInter + (ener*betaLGSlope) + (iList*betaLGISI) + (ener*iList*betaLGInteraction) + betaLGError
MAPCI_LLG = betaLGInterCI[0] + (ener*betaLGSlopeCI[0]) + (iList*betaLGISICI[0]) + (ener*iList*betaLGInteractionCI[0]) + betaLGErrorCI[0]
MAPCI_HLG = betaLGInterCI[1] + (ener*betaLGSlopeCI[1]) + (iList*betaLGISICI[1]) + (ener*iList*betaLGInteractionCI[1]) + betaLGErrorCI[1]

plt.scatter(lepp,lg)
plt.plot(ener,MAPLG,'g')
plt.plot(ener,MAPCI_LLG,'r')
plt.plot(ener,MAPCI_HLG,'r')
plt.title('Low Gamma Band')
plt.show()
pdb.set_trace()