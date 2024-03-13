function [kmedian,p,q]=z1test(x,sig)

if nargin<2
    sig=1;
end

s=size(x);
if s(2)==1
    x=x';
end
N=length(x); j=[1:N];
t=[1:round(N/10)];
M=zeros(1,round(N/10));
c=pi/5+rand(1,100)*4*pi/5;
for its=1:100
    p=cumsum(x.*cos(j*c(its)));q=cumsum(x.*sin(j*c(its)));
    for n=1:round(N/10)
        M(n)=mean( (p(n+1:N)-p(1:N-n)).^2 + (q(n+1:N)-q(1:N-n)).^2 )- ...
            mean(x)^2*(1-cos(n*c(its)))/(1-cos(c(its)))+sig*(rand-.5);
    end
    kcorr(its)=corr(t',M');
end
kmedian=median(kcorr);
end