import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pdb
#import arviz as az
#import pymc as pm
#import aesara
import matplotlib.pyplot as plt
import pdb
#from mpl_toolkits.mplot3d import Axes3D
import json
import pickle # python3
import seaborn as sns
from sklearn.cluster import OPTICS, cluster_optics_dbscan, KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
randomSeed = 777
color = '#87ceeb'
def addMIDF(df1,df2):
    [df1Size,col] = np.shape(df1)
    [df2Size,col] = np.shape(df2)
    dfNVec1 = []
    dfNVec2 = []
    for ck in range(df1Size):
        dfNVec1.append(str(df1['DataID'][ck]) + str(df1['Electrode'][ck]) + str(df1['EnergyPerPulse'][ck]) + str(df1['ISI'][ck]) + str(df1['NPulses'][ck]))
    for ck in range(df2Size):
        dfNVec2.append(str(df2['DataID'][ck]) + str(df2['Electrode'][ck]) + str(df2['EnergyPerPulse'][ck]) + str(df2['ISI'][ck]) + str(df2['NPulses'][ck]))
    MIVector = np.zeros((df1Size,))
    
    if df1Size < df2Size:
        for ck in range(df1Size):
            for bc in range(df2Size):
                if dfNVec1[ck] == dfNVec2[bc]:
                    
                    MIVector[ck] = df2['MI'][bc]
                    break
    df = df1.assign(MI=MIVector)
    return df
#Have two dataframes due to analysis code splitting data.
#df = pd.read_pickle('LFPChaos3.pkl')
df1 = pd.read_pickle('LFPChaosMKIV.pkl')
df2 = pd.read_pickle('LFPChaosMKV.pkl')
df3 = pd.read_pickle('LFPMI.pkl')
df = pd.concat([df1, df2], ignore_index=True, sort=False)
df = addMIDF(df,df3)


# if __name__ == '__main__':
#     with pm.Model() as Heirarchical_Regression:
#         # Hyperpriors for group nodes
#         mu_a = pm.Normal("mu_a", mu=0.0, sigma=1)
#         sigma_a = pm.HalfNormal("sigma_a", 1)
#         mu_b = pm.Normal("mu_b", mu=0.0, sigma=1)
#         sigma_b = pm.HalfNormal("sigma_b", 1)
        
#         sigma_nu = pm.Exponential("sigma_nu",5.0)
#         #Base layer
#         nu = pm.HalfCauchy('nu', sigma_nu)          #Nu for robust regression
#         a_offset = pm.Normal('a_offset', mu=0, sigma=1, shape=(n_channels))
#         a = pm.Deterministic("a", mu_a + a_offset * sigma_a)

#         b1_offset = pm.Normal('b1_offset', mu=0, sigma=1, shape=(n_channels))
#         b1 = pm.Deterministic("b1", mu_b + b1_offset * sigma_b)

#         eps = pm.HalfCauchy("eps", 5,shape=(n_channels))

#         regression = a[animalID] + (b1[animalID] * lepp) 

#         likelihood = pm.StudentT("MaxZ_like",nu=nu,mu=regression,sigma=eps[animalID], observed= MI) 

#     """
#     Now we run the model!
#     """
#     with Heirarchical_Regression:
#         if __name__ == '__main__':
#                 step = pm.NUTS()
#                 rTrace = pm.sample(numSamples, tune=numBurnIn, target_accept=0.90,chains = 4,  nuts_sampler="numpyro")
#                 #rTrace = pm.sampling_jax.sample_numpyro_nuts(numSamples, tune=numBurnIn, target_accept=0.95,chains = 4)
#     """
#     Now do model analytics
#     """
#     intercept = rTrace.posterior["a"]                #Grab the posterior distribution of a
#     EnergySlope = rTrace.posterior["b1"]                    #Grab the posterior distribution of b1
#     err = rTrace.posterior["eps"]                    #Grab the posterior distribution of model error
#     f_dict = {'size':16}
    
#     fig, ([ax1, ax2, ax3], [ax4, ax5, ax6]) = plt.subplots(2,3, figsize=(12,6))
#     for ax, estimate, title, xlabel in zip(fig.axes,
#                                 [intercept, EnergySlope, err],
#                                 ['Intercept', 'Energy Slope','Error Parameter'],
#                                 [r'$a$', r'$\beta1$', r'$err$']):
#         pm.plot_posterior(estimate, point_estimate='mode', ax=ax, color=color,hdi_prob=0.95)
#         ax.set_title(title, fontdict=f_dict)
#         ax.set_xlabel(xlabel, fontdict=f_dict)
#     plt.show()
#     with Heirarchical_Regression:
#         pm.compute_log_likelihood(rTrace)
    
#     with Heirarchical_Regression:
#         if __name__ == '__main__':
#             ppc = pm.sample_posterior_predictive(rTrace, random_seed=randomSeed)

    # az.plot_bpv(ppc, hdi_prob=0.95,kind='p_value')
    # az.plot_ppc(ppc)



df12 = df.loc[df['Stochastic']==0]
df12.reset_index(drop=True, inplace = True)
# df13 = df2.loc[df2['Stochastic']==0]
# df13.reset_index(drop=True, inplace = True)
energy12 = df12.EnergyPerPulse.values
energy12 = energy12.astype(float)
energy12[energy12<0]=0
# energy13 = df13.EnergyPerPulse.values
# energy13 = energy13.astype(np.float)
# energy13[energy13<0]=0
# #energyK = energy12
# energyK = np.concatenate((energy12,energy13))
# K1 = df12.KChaos
# K2 = df13.KChaos
#K = K1
K = df12['KChaos'].values

#MIK = MIK1
MIK = df12.MI.values
plt.scatter(np.log(MIK+0.001),K)
plt.show()
dataID = []
electrodes = []
for ck in range(len(energy12)):
    dataID.append(df12.DataID[ck])
    electrodes.append(df12.Electrode[ck])

animalID = np.zeros((len(energy12),),dtype=int)
IDXList = {}
countIDX = 0
X = np.vstack((np.log(MIK+0.001),K))
X = np.transpose(X)
range_n_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for n_clusters in range_n_clusters:
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(X)
    silhouette_avg = silhouette_score(X, cluster_labels)
    print(
        "For n_clusters =",
        n_clusters,
        "The average silhouette_score is :",
        silhouette_avg,
    )
pdb.set_trace()
#clust = OPTICS(min_samples=5, xi=0.05, min_cluster_size=0.4)
clust = KMeans(init="k-means++", n_clusters=2)
clust.fit(X)
pdb.set_trace()
h = 0.02  # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = X[:, 0].min()-0.1 , X[:, 0].max() +0.1
y_min, y_max = X[:, 1].min()-0.1 , X[:, 1].max() +0.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = clust.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(
    Z,
    interpolation="nearest",
    extent=(xx.min(), xx.max(), yy.min(), yy.max()),
    cmap=plt.cm.Paired,
    aspect="auto",
    origin="lower",
)
plt.scatter(np.log(MIK+0.001),K)
plt.xlabel('ln(Mutual Information) (bits)')
plt.ylabel('Chaos K-statistic')
plt.show()
# colors = ["g.", "r."]
# for klass, color in zip(range(0, 5), colors):
#     Xk = X[clust.labels_ == klass]
#     plt.plot(Xk[:, 0], Xk[:, 1], color, alpha=0.3)
# plt.plot(X[clust.labels_ == -1, 0], X[clust.labels_ == -1, 1], "k+", alpha=0.1)
# plt.show()
# for ck in range(len(energy12)):

#     IDX = dataID[ck].split('//')
#     curIDX = IDX[0]
#     elec = electrodes[ck]
#     keyIDX = curIDX+str(elec)
#     if keyIDX in IDXList.keys():
#         animalID[ck] = int(IDXList[keyIDX])
#     else:
#         animalID[ck] = int(countIDX)
#         IDXList[keyIDX] = int(countIDX)
#         countIDX = countIDX+1
# n_channels = len(np.unique(animalID))
# if __name__ == '__main__':
#     with pm.Model() as Heirarchical_Regression:
#         # Hyperpriors for group nodes
#         mu_a = pm.Normal("mu_a", mu=0.0, sigma=1)
#         sigma_a = pm.HalfNormal("sigma_a", 1)
#         mu_b = pm.Normal("mu_b", mu=0.0, sigma=1)
#         sigma_b = pm.HalfNormal("sigma_b", 1)
#         sigma_nu = pm.Exponential("sigma_nu",5.0)
#         #Base layer
#         nu = pm.HalfCauchy('nu', sigma_nu)          #Nu for robust regression
#         a_offset = pm.Normal('a_offset', mu=0, sigma=1)
#         a = pm.Deterministic("a", mu_a + a_offset * sigma_a)

#         b1_offset = pm.Normal('b1_offset', mu=0, sigma=1)
#         b1 = pm.Deterministic("b1", mu_b + b1_offset * sigma_b)
#         eps = pm.HalfCauchy("eps", 5)

#         regression = a + (b1 * np.log(MIK+0.001))

#         likelihood = pm.StudentT("MaxZ_like",nu=nu,mu=regression,sigma=eps, observed= K) 

#     """
#     Now we run the model!
#     """
#     with Heirarchical_Regression:
#         if __name__ == '__main__':
#                 step = pm.NUTS()
#                 rTrace = pm.sample(numSamples, tune=numBurnIn, target_accept=0.90,chains = 4, nuts_sampler="numpyro")
#                 #rTrace = pm.sampling_jax.sample_numpyro_nuts(numSamples, tune=numBurnIn, target_accept=0.95,chains = 4)
#     """
#     Now do model analytics
#     """
#     intercept = rTrace.posterior["a"]                #Grab the posterior distribution of a
#     EnergySlope = rTrace.posterior["b1"]                    #Grab the posterior distribution of b1
#     err = rTrace.posterior["eps"]                    #Grab the posterior distribution of model error
#     f_dict = {'size':16}
    
#     fig, ([ax1, ax2, ax3], [ax4, ax5, ax6]) = plt.subplots(2,3, figsize=(12,6))
#     for ax, estimate, title, xlabel in zip(fig.axes,
#                                 [intercept, EnergySlope, err],
#                                 ['Intercept', 'Energy Slope','Error Parameter'],
#                                 [r'$a$', r'$\beta1$', r'$err$']):
#         pm.plot_posterior(estimate, point_estimate='mode', ax=ax, color=color,hdi_prob=0.95)
#         ax.set_title(title, fontdict=f_dict)
#         ax.set_xlabel(xlabel, fontdict=f_dict)
#     plt.show()
#     with Heirarchical_Regression:
#         pm.compute_log_likelihood(rTrace)
    
#     with Heirarchical_Regression:
#         if __name__ == '__main__':
#             ppc = pm.sample_posterior_predictive(rTrace, random_seed=randomSeed)

#     az.plot_bpv(ppc, hdi_prob=0.95,kind='p_value')
#     az.plot_ppc(ppc)
# plt.show()
pdb.set_trace()
