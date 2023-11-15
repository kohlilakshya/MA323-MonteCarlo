import numpy as np
import matplotlib.pyplot as plt
from numpy import random

x = list()
p = 0.3
for i in range(1000000):
    u = np.random.uniform(0,1)
    y = np.log(u)/np.log(1-p)
    x.append(np.floor(y))
plt.hist(x, bins=100, density=True)
plt.show()
