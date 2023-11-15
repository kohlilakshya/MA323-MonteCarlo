# It would be better if each questions's code is executed
# seperately with the same header for all. 
# If not, the plots will overlap.

import numpy as np
import matplotlib.pyplot as plt
import cmath 
import math 
from numpy import random

# answer1
# lcg
def generator1(a, b, m, x0):
    ui = list()
    x = x0
    for i in range(17):
        x = (a * x + b) % m
        u = x/m
        ui.append(u)
    return ui

# recursion
def rec(n, sequence):
    for i in range (17, n):
        u = sequence[i-17] - sequence[i-5]
        if u < 0:
            u = u+1
        sequence.append(u)
    return sequence

#histogram
def ans(a,b,m,x0,n):
    sequence = generator1(a,b,m,x0)
    x = rec(n, sequence)
    y = x.copy()
    plt.hist(x, bins= np.arange(min(x), max(x) + 0.01 , 0.01)) 
    plt.xlabel("Ui")
    plt.ylabel("Frequency")
    plt.title(f"Answer1.c: Histogram for n = {n}")
    plt.show()
    # plt.savefig("q1c n = " + str(n))

    del x[len(x) - 1]
    del y[0]

    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.5)
    plt.xlabel("U i-1")
    plt.ylabel("U i")
    plt.title(f"Answer 1.d: Two Dimensional plot n = {n}")
    plt.show()
    # plt.savefig("q1d n = " + str(n))

#answer 1
for i in [1000,10000,100000]:
    ans(1229, 1, 2048, 1, i)


#--------------------------------------------------------------------

# answer 2
n_values = [10, 100, 1000, 10000, 100000]
for n in n_values:
    np.random.seed(42)
    sequence = random.uniform(0,1,n)
    print(len(sequence))

    theta = 2
    X = list()

    for i in sequence:
        x = -theta * math.log(1 - i)
        X.append(x)

    sorted_Y = np.sort(X)
    y_val = np.arange(len(sorted_Y))/float(len(sorted_Y) - 1)

    plt.title(f'Distribution Function for n = {n}')
    plt.ylabel('Probability : P(X <= x)')
    plt.xlabel('X')
    plt.plot(sorted_Y, y_val, color='blue')
    plt.savefig("q2b n = "+ str(n))
    # plt.show()

    print("Sample Size = ", n)
    print("Mean =", np.mean(X))
    print("Variance =", np.var(X))
    print()


x = np.arange(0, 25, 0.01)
Fx = list()
for i in x:
    Fx.append(1-np.exp(-i/theta))

plt.plot(x, Fx, color='green')
plt.title('Actual Distribution Function')
plt.ylabel('F(x) ')
plt.xlabel('x')
plt.savefig("q2d")
plt.show()

print("Theoretical Mean =", theta)
print("Theoretical Variance =", theta*theta)

#--------------------------------------------------------------------
#Answer 3
# n_values = [10, 100, 1000, 10000, 100000]

def temp(n):
    np.random.seed(16)
    sequence = random.uniform(size=n) 
    print(len(sequence))

    X = list()
    for i in sequence:
        val = 0.5 - 0.5*math.cos(i*cmath.pi)
        X.append(val)

    sorted_Y = np.sort(X)
    y_val = np.arange(len(sorted_Y))/float(len(sorted_Y) - 1)
    
    plt.title('Distribution Function of X ( sample count = {} )'.format(n))
    plt.ylabel('Probability - P(X <= x)')
    plt.xlabel('X (generated values)')
    plt.plot(sorted_Y, y_val, color='blue')
    plt.savefig('q3b n = ' + str(n))
    #   plt.show()
    
    print("Sample Size = ", n)
    print("Mean = ", np.mean(X))
    print("Variance = ", np.var(X))
    print()


for n in n_values:
    temp(n)

x = np.arange(0, 1.001, 0.01)
Fx = list()
for i in x:
    Fx.append((2/cmath.pi)*math.asin(math.sqrt(i)))

import matplotlib.pyplot as plt
plt.plot(x, Fx, color='green')
plt.title('Actual Distribution Function')
plt.ylabel('F(x)')
plt.xlabel('x')
plt.savefig('q3 actual')


#--------------------------------------------------------------------
#Answer 4
np.random.seed(0)
a = random.uniform(0, 1, 100000) 
print(len(a))

X = list()
q = dict()
for i in range(0, 10001):
        q[i] = 0

range_value = dict()
for j in range(20):
    range_value[j] = 0

for i in a:
    val = math.floor(i*10000)
    if val % 2 == 0  and val != 0:
        val -= 1
    if val!= 0:
        X.append(val)
        q[val] += 1
        t = np.floor(val/500)
        range_value[t]+=1

keys = list(q.keys())
values = list(q.values())

print(range_value)

plt.bar(keys, values)
plt.xlabel('X value')
plt.ylabel('Frequency')
# plt.show()
plt.savefig('q4')

