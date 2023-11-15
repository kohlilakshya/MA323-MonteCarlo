import numpy as np
import matplotlib.pyplot as plt
from numpy import random

X= list()
while len(X) < 10000:
    u = np.random.uniform(0,1)
    y = -np.log(u)
    z = 1
    probab = np.random.uniform(0,1)
    if probab<1/2:
        z = -1
    x = y*z
    u1 = np.random.uniform(0,1)
    if u1*np.exp((1-2*abs(x))/2) <= np.exp(-.5*x**2):
        X.append(x)

print(len(X))
plt.hist(X, bins=100, density=True)
plt.show()