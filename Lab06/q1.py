import numpy as np
import math
from numpy import random
from scipy.stats import norm

m_values = [100,1000,10000,100000]

# Confidence Intervals
alpha = 0.05  # 5% significance level
delta = norm.ppf(1 - alpha / 2)

for m in m_values:
    Y = list()
    np.random.seed(16)
    for i in range(m):
        u = np.random.uniform(0,1)
        t = math.exp(math.sqrt(u))
        Y.append(t)
    Im = np.mean(Y)
    sm_squre = 0
    for i in range(m):
        sm_squre+= math.pow(Im-Y[i],2)
    sm_squre/=(m-1)
    sm = math.sqrt(sm_squre)

    L = (Im) - (delta*sm/math.sqrt(m))
    U = (Im) + (delta*sm/math.sqrt(m))

    print("For m = {}".format(m))
    print("Im \t\t\t= {}".format(Im))
    print("Confidence Interval \t= [{}, {}]".format(L, U))
    print("Variance \t\t= {}".format(sm*sm))
    print()