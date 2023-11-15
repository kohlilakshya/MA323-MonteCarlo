import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import random

def fx(alpha1, alpha2, x):
    t = math.gamma(alpha1)*math.gamma(alpha2)/math.gamma(alpha1+alpha2)
    return math.pow(x, alpha1-1)*math.pow(1-x, alpha2-1)/t

x = list()
alpha1 = 2
alpha2 = 8

c = fx(alpha1, alpha2, (alpha1-1)/(alpha1+alpha2-2))

while len(x)<100000:
    u1 = np.random.uniform(0,1)
    u2 = np.random.uniform(0,1)
    if u2*c<=fx(alpha1, alpha2,u1):
        x.append(u1)

plt.hist(x, bins=100, density=True)
plt.show()