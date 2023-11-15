import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import random

def fraction(alpha):
    u1 = np.random.uniform()
    A = (1/np.exp(1)) + (1/alpha)
    c = A/math.gamma(alpha)
    if u1*alpha*A<1:
        x = math.pow(u1*alpha*A, 1/alpha)
        u2 = np.random.uniform(0,1)
        if u2 <= np.exp(-x)/A:
            return x
        else:
            return fraction(alpha)
    else:
        x = -np.log(A)-np.log(1-u1)
        u2 = np.random.uniform(0,1)
        if u2 <= math.pow(x, alpha-1):
            return x
        else:
            return fraction(alpha)
        

def integer(alpha):
    n = alpha
    y = 0
    while n != 0:
        u = np.random.uniform(0, 1)
        t = -np.log(u)
        y = y + t
        n = n - 1
    return y

def gamma(alpha,n):
    x = list()
    if alpha == int(alpha):
        for i in range(n):
            x.append(integer(alpha))
        
    elif alpha>0 and alpha<1:
        for i in range(n):
            x.append(fraction(alpha))
    else:
        alpha1 = int(alpha)
        alpha2 = alpha - alpha1

        for i in range(n):
            x.append(integer(alpha1) + fraction(alpha2))

    return x

def beta(alpha1, alpha2,n):
    Z = list()
    x = gamma(alpha1,n)
    y = gamma(alpha2,n)
    for i in range(n):
        Z.append(x[i]/(x[i]+y[i]))
    return Z

alpha1 = 2
alpha2 = 8
n = 10000
z = beta(alpha1, alpha2, n)
plt.hist(z, bins = 100, density=True)
plt.show()