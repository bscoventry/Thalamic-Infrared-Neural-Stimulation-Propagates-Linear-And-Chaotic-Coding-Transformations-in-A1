function [mWaveVel,sWaveVel,prctVar,absUav]=batchWavePatt()
addpath(genpath('Filtering'));
addpath(genpath('InDevelopment'));
addpath(genpath('OpticalFlow'));
addpath(genpath('SimulatedData'));
addpath(genpath('Visualisation'))
addpath(genpath('PatternDetection'))
params = setNeuroPattParams(1526);
fs = 1526;
LFP = load('LFP1.mat');
LFP = LFP.LFP;
results = mainProcessingWithOutput(LFP,fs,params);
mWaveVel = results.mVFS;
sWaveVel = results.sVFS;
prctVar = results.prctVar;
absUav = results.absUav;
pvals = results.pvals;
sig = find(pvals<=0.05);
if length(sig)>0
    [nc,nr] = size(pvals);
    transitionMatrix = zeros(nc*nr,1);
    transitionMatrix(sig) = 1;
else
    transitionMatrix = -1;
end


