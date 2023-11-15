import numpy as np
from numpy import random

np.random.seed(42)

def bray(n):
    Z1 = list()
    u1 = np.random.uniform(0,1)
    u2 = np.random.uniform(0,1)
    u1 = 2*u1 - 1
    u2 = 2*u2 - 1
    p = u1*u1 + u2*u2
    if p <= 1:
        Z1.append(u1*np.sqrt((-2*np.log(p))/p))
    return Z1

def norm(mu, sigma, n):
    Z1 = bray(n)
    z = list()
    for i in range(n):
        z.append(mu + sigma*Z1[i])
    return z


