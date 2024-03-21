function [mWaveVel,transitionMatrix]=batchWavePatt(LFP,fs)
addpath(genpath('Filtering'));
addpath(genpath('InDevelopment'));
addpath(genpath('OpticalFlow'));
addpath(genpath('SimulatedData'));
addpath(genpath('Visualisation'))
addpath(genpath('PatternDetection'))
load('params.mat');
results = mainProcessingWithOutput(LFP,fs,params);
mWaveVel = results.maxVelocityVal;
pvals = results.pvals;
sig = find(pvals<=0.05);
if length(sig)>0
    [nc,nr] = size(pvals);
    transitionMatrix = zeros(nc*nr,1);
    transitionMatrix(sig) = 1;
else
    transitionMatrix = -1;
end


