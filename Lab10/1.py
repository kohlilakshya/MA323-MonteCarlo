import numpy as np
import matplotlib.pyplot as plt
import math

def generator_VanCorput(n, base):
    X = list()
    for i in range(n):
        loop=i
        x = 0
        p=-1
        while(loop>0):
            x = x+ (loop%base)*(base**p)
            loop = (int)(loop/base)
            p=p-1
        X.append(x)
    return X

def generator_lcg(n):
    x0 = 7
    a = 1229
    b = 1
    m = 2048
    u = list()
    u.append(x0/m)
    for i in range(n):
        x0 = (a * x0 + b) % m
        u.append(x0/m)
    return u

van_seq25 = generator_VanCorput(25,2)
print(van_seq25)

van_seq1000=generator_VanCorput(1000,2)
xi=van_seq1000[0:999]
xi1=van_seq1000[1:1000]
plt.scatter(xi,xi1) #plotting the (x(i),x(i+1)) points on a graph
plt.title('(x(i),x(i+1)) for 1000 values of Van der Corput sequence')
plt.xlabel('x(i) values')
plt.ylabel('x(i+1) values')
plt.show()

van_seq100=generator_VanCorput(100,2)
van_seq100000=generator_VanCorput(100000,2)

print('LCG used: x(i+1)=(1229*x(i)+1)%2048 with x(0)=7')
lcg100=generator_lcg(100)
lcg100000=generator_lcg(100000)

fig = plt.figure(figsize= (15, 10))
plot_1 = fig.add_subplot(221)
plot_1.hist(van_seq100,bins=25,rwidth=0.75)
plot_1.set_title('100 values of Van der Corput sequence')
plot_1.set_xlabel('values')
plot_1.set_ylabel('frequency')

plot_2 = fig.add_subplot(222)
plot_2.hist(lcg100,bins=25,rwidth=0.75)
plot_2.set_title('100 values using LCG')
plot_2.set_xlabel('values')
plot_2.set_ylabel('frequency')

plot_3 = fig.add_subplot(223)
plot_3.hist(van_seq100000,bins=25,rwidth=0.75)
plot_3.set_title('100000 values of Van der Corput sequence')
plot_3.set_xlabel('values')
plot_3.set_ylabel('frequency')

plot_4 = fig.add_subplot(224)
plot_4.hist(lcg100000,bins=25,rwidth=0.75)
plot_4.set_title('100000 values using LCG')
plot_4.set_xlabel('values')
plot_4.set_ylabel('frequency')

plt.show()


f2_100 = generator_VanCorput(100,2)
f2_100000 = generator_VanCorput(100000,2)
f3_100 = generator_VanCorput(100,3)
f3_100000 = generator_VanCorput(100000,3)

#plotting the (f2(i), f3(i)) points on a graph for 100 values
plt.scatter(f2_100, f3_100) 
plt.title('(φ2(i), φ3(i)) for 100 values of Halton sequence')
plt.xlabel('φ2(i) values')
plt.ylabel('φ3(i) values')
plt.show()

#plotting the (φ2(i), φ3(i)) points on a graph for 100000 values
plt.scatter(f2_100000, f3_100000) 
plt.title('(φ2(i), φ3(i)) for 100000 values of Halton sequence')
plt.xlabel('φ2(i) values')
plt.ylabel('φ3(i) values')
plt.show()

