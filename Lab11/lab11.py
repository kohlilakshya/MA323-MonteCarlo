import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import random
np.random.seed(42)

def bray(n):
    z1 = list()
    while len(z1) < n:
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1)
        u1 = 2*u1 - 1
        u2 = 2*u2 - 1
        p = math.pow(u1, 2) + math.pow(u2, 2)
        if p <= 1:
            denom = p
            numer = -2*np.log(denom)
            z1.append(u1*math.pow(numer/denom, 1/2))
    return z1

n = 5000

# 1
pi_values = [1/2, 1/3, 1/6]
mu_values = [-1,0,1]
sigma_values = [1/4, 1, 1/2]
q_values = list()
q_values.append(0)

for i in range(len(pi_values)):
    q_values.append(pi_values[i]+q_values[i])


X = list()
for i in range(n):
    u = np.random.uniform(0,1)
    for j in range(len(q_values)-1):
        if q_values[j] < u and u<=q_values[j+1]:
            x = mu_values[j] + sigma_values[j]*bray(1)[0]
            X.append(x)
            break
print(f"The average of the generated random numbers is {np.mean(X)}")

#2 & 3 
w10 = list()
x10 = list()
x0 = 5
mu = 0.06
sigma = 0.3
t_values = list()
for i in range(n+1):
    t_values.append(i*5/5000)

plt.title("Brownian Paths")
for i in range(10):
    wi = list()
    wi.append(0)
    xi = list()
    xi.append(x0)
    Z = bray(n)
    for j in range(n):
        w = wi[j] + np.sqrt(t_values[j+1]-t_values[j])*Z[j]
        x = xi[j] + mu*(t_values[j+1]-t_values[j]) + sigma*np.sqrt(t_values[j+1]-t_values[j])*Z[j]
        wi.append(w)
        xi.append(x)
    w10.append(wi)
    x10.append(xi)
    plt.plot(t_values,wi, label=f"Sample Path {i+1}")
    plt.legend()
plt.show()

meanW2 =  0
meanW5 = 0
for i in range(10):
    meanW2 += w10[i][2000]
    meanW5 += w10[i][5000]
meanW2 /=10
meanW5 /=10
print(f"Estimate of E[W(2)] = {meanW2}")
print(f"Estimate of E[W(5)] = {meanW5}")

# 3
plt.title("Brownian motion (BM(\u03BC,\u03C3\u00b2)) discretization")
for i in range(10):
    plt.plot(t_values,x10[i], label=f"{i+1}")
    plt.legend()
plt.show()

meanX2 =  0
meanX5 = 0
for i in range(10):
    meanX2 += x10[i][2000]
    meanX5 += x10[i][5000]
meanX2 /=10
meanX5 /=10
print(f"Estimate of E[X(2)] = {meanX2}")
print(f"Estimate of E[X(5)] = {meanX5}")
