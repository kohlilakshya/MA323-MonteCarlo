import numpy as np
import math
import matplotlib.pyplot as plt
np.random.seed(42)

def bray(n):
    Z = list()
    while len(Z) < n:
        u1 = np.random.uniform(0,1)
        u2 = np.random.uniform(0,1)
        u1 = 2*u1 -1
        u2 = 2*u2 -1
        p = u1*u1 + u2*u2
        if p <=1:
            Z.append(u1*np.sqrt(-2*np.log(p)/p))
    
    return Z

n = 10000
Z = bray(n)
count = 0
for z in Z:
    if z > 4:
        count+=1
probab = count/n
print(probab)

sn_square = 0
for z in Z:
    if z > 4:
        sn_square += (1-probab)**2
    if z <= 4:
        sn_square += (probab)**2
sn_square /=(n-1)
print(sn_square)

# imp
def p(x):
    return np.exp(-0.5*x**2)/np.sqrt(2*np.pi)
def q(x):
    return np.exp(-(x-4))

Z_imp = list()
for i in range(n):
    u = np.random.uniform(0,1)
    z = -np.log(1-u) + 4
    print(z)
    if z > 4:
        Z_imp.append(p(z)/q(z))
    else:
        Z_imp.append(0)

probab_imp = np.mean(Z_imp)
print(probab_imp)

sn_square_imp = 0
for z in Z_imp:
    sn_square_imp += (z-probab_imp)**2

sn_square_imp /=(n-1)
print(sn_square_imp)