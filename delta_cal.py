from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import math

np.random.seed(42)
n = 1000
X = list()

for i in range(n):
    u = np.random.uniform(0,1)
    if u <= 0.2:
        u1 = np.random.uniform(0,1)
        X.append(-np.log(1-u1)/2)
    else:
        X.append(0)

print(np.mean(X))

plt.hist(X, bins = 'auto', density= True)
plt.show()