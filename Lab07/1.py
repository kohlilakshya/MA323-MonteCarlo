import numpy as np
import math
from scipy.stats import norm

n_values = [100,1000,10000,100000]

# Confidence Intervals
alpha = 0.05  # 5% significance level
delta = norm.ppf(1 - alpha / 2)

for n in n_values:
    Y = list()
    np.random.seed(16)
    m = int(n/2)
    for i in range(m):
        u = np.random.uniform(0,1)
        t = (math.exp(math.sqrt(u))+ math.exp(math.sqrt(1-u)))/2
        Y.append(t)
    Im = np.mean(Y)
    sm_sq = 0
    for i in range(m):
        sm_sq+= math.pow(Y[i]-Im,2)
    sm_sq /= (m-1)
    sm = math.sqrt(sm_sq)
   
    L = (Im) - (delta*sm/math.sqrt(m))
    U = (Im) + (delta*sm/math.sqrt(m))

    print("For n = {}".format(n))
    print("Im \t\t\t= {}".format(Im))
    print("Confidence Interval \t= [{}, {}]".format(L, U))
    print("Variance \t\t= {}".format(sm*sm))
    print("Interval Length \t= {}".format(U-L))
    print()