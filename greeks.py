import numpy as np
from scipy.stats import norm
from black_scholes import d1, d2


def delta(S,K,T,r,sigma):
    return norm.cdf(d1(S,K,T,r,sigma))


def gamma(S,K,T,r,sigma):
    return norm.pdf(d1(S,K,T,r,sigma)) / (S*sigma*np.sqrt(T))


def vega(S,K,T,r,sigma):
    return S*norm.pdf(d1(S,K,T,r,sigma))*np.sqrt(T)


def theta(S,K,T,r,sigma):
    term1 = -(S*norm.pdf(d1(S,K,T,r,sigma))*sigma)/(2*np.sqrt(T))
    term2 = -r*K*np.exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
    return term1 + term2
