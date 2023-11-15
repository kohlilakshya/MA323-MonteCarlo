import numpy as np
import matplotlib.pyplot as plt
import math
np.random.seed(42)

# theta = 2
# n_values = [10, 100, 1000, 10000, 100000]

# Fx = list()
# x = np.arange(0,20, 0.01)
# for i in x:
#     Fx.append(1-np.exp(-i/theta))
# plt.plot(x, Fx)
# plt.show()

# for n in n_values:
#     X = list()
#     for i in range(n):
#         u = np.random.uniform(0,1)
#         X.append((np.sin(u*np.pi/2))**2)

#     plt.hist(X, bins = 'auto', density= True)
#     plt.show()

n = 100000
X = list()
q = dict()
for i in range(10000):
    q[i] = 0

for i in range(n):
    u = np.random.uniform(0,1)
    val = math.floor(u*10000)
    if val%2 ==0 and val!=0:
        val-=1
    if val!=0:
        X.append(val)
        q[val]+=1 

keys = list(q.keys())
values = list(q.values())

plt.bar(keys, values)
plt.show()