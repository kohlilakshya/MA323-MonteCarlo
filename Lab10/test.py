import numpy as np
import matplotlib.pyplot as plt
import math

def van(n, base):
    X = list()
    for i in range(n):
        loop = i
        p = -1
        x = 0
        while(loop>0):
            x += (loop%base)*math.pow(base,p)
            loop = int(loop/base)
            p-=1
        X.append(x)
    return X

def f1(x):
    return x

def f2(x):
    return x**2

x1 = np.linspace(0,100,1000)
y1 = list()
y2 = list()

for i in range(1000):
    y1.append(f1(x1[i]))
    y2.append(f2(x1[i]))


plt.figure(figsize=(15,10))
plt.subplot(2,2,3)
plt.plot(x1,y1, label = "f1")
plt.title("hello ji")
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(x1,y2, label = "f1")
plt.title("hello ji")
plt.grid(True)

plt.show()