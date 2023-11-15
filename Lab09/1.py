import numpy as np
from numpy import random
import math
import matplotlib.pyplot as plt
from scipy.stats import norm, skew

np.random.seed(17)

def generate_exp(theta):
    lambda_parameter = 1/theta
    u = np.random.uniform()
    X = (-np.log(1-u)/lambda_parameter)
    return X

def generate_E10(theta, n):
    E_10 = list()
    count = 0
    for i in range(n):
        T1 = generate_exp(theta[0])
        T2 = generate_exp(theta[1])
        T3 = generate_exp(theta[2])
        T4 = generate_exp(theta[3])
        T5 = generate_exp(theta[4])
        T6 = generate_exp(theta[5])
        T7 = generate_exp(theta[6])
        T8 = generate_exp(theta[7])
        T9 = generate_exp(theta[8])
        T10 = generate_exp(theta[9])

        E1 = T1
        E2 = T1 + T2
        E3 = T1 + T3
        E4 = T1 + T2 + T4
        E5 = T1 + T2 + T5
        E6 = T1 + T3 + T6
        E7 = T1 + T3 + T7
        E8 = T1 + T3 + T8
        E9 = max(E5, E6, E7) + T9
        E10 = max(E4, E8, E9) + T10

        E_10.append(E10)
        if E10 >70:
            count+=1
    return E_10, count

n = 10000
theta = [4, 4, 2, 5, 2, 3, 2, 3, 2, 2]

E_10, count = generate_E10(theta, n)
mean_E10 = np.mean(E_10)
var_E10 = np.var(E_10)
variance_E10_monte = var_E10
#b
print(f'The observed mean of E10 = {mean_E10}') 
#d
print(f'The observed standard deviation of E10 = {np.sqrt(var_E10)}')
print(f'An approximate value of the probability that the project miss the deadline using simple Monte Carlo = {count/n}')

#c
plt.hist(E_10, bins=100, density=True, alpha=0.6, color='blue', label='E10 Distribution')
plt.xlabel('')
plt.ylabel('E10')
plt.title(f'Histogram of generated values of E10') 
plt.legend()
print(f"Skewness of samples is {skew(E_10)}")
# plt.show()

print()

#e
lambda_ = list()

for i in theta:
    lambda_.append(i*4)

E_10, count = generate_E10(lambda_, n)
mean_E10 = np.mean(E_10)
var_E10 = np.var(E_10)
sample_size = (variance_E10_monte/var_E10)*n
print(f'The observed mean of E10 = {mean_E10}') 
print(f'The observed standard deviation of E10 = {np.sqrt(var_E10)}')
print(f'An approximate value of the probability that the project miss the deadline using importance sampling = {count/n}')
print(f'Effective Sample Size = {sample_size}') 
print()

#f
lamda_ = theta
k_values = [3,4,5]
mini_ss = n**4
mini_k = 0
mean_ = 0
var_ = 0
for k in k_values:
    print(f'for k = {k}')
    for i in range(len(theta)):
        if(i==0 or i == 1 or i == 3 or i == 9):
            lamda_[i] = k*theta[i]

    E_10, count = generate_E10(lambda_, n)
    mean_E10 = np.mean(E_10)
    var_E10 = np.var(E_10)
    sample_size = (variance_E10_monte/var_E10)*n
    print(f'The observed mean of E10 = {mean_E10}') 
    print(f'The observed standard deviation of E10 = {np.sqrt(var_E10)}')
    print(f'An approximate value of the probability that the project miss the deadline using importance sampling = {count/n}')
    print(f'Effective Sample Size = {sample_size}') 
    if sample_size <mini_ss:
        mini_ss = sample_size
        mini_k = k
        mean_ = mean_E10
        var_ = var_E10
    print()

#h
print(f"k = {mini_k} has the minimum effective sample size.")
L = mean_ - 2.58*np.sqrt(var_)/np.sqrt(n)
U = mean_ + 2.58*np.sqrt(var_)/np.sqrt(n)
print(f"99% Confidence interval {(L, U)}")