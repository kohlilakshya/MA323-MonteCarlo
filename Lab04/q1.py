import numpy as np
import matplotlib.pyplot as plt
import time
import math
from scipy.stats import norm
from numpy import random

def N(n):

    seq1 = box_muller(n)
    seq2 = bray(n)
    mu_values = [0,5]
    sigma_sq = 5
    for mu in mu_values:
        seq1y = list()
        seq2y = list()
        for i in range(n):
            seq1y.append(mu + np.sqrt(sigma_sq)*seq1[i])
            seq2y.append(mu + np.sqrt(sigma_sq)*seq2[i])

        plt.hist(seq1y, bins=100, density=True, alpha=0.6, color='red', label='Observed Distribution')
        plt.xlabel('X')
        plt.ylabel('Probability Density')
        plt.title(f'Frequency Distribution of Sampled Values (N({mu},{sigma_sq}), {n} samples) (Box-Muller)')
        plt.legend()

        x = np.linspace(mu - 3*np.sqrt(sigma_sq), mu + 3*np.sqrt(sigma_sq), 1000)
        y = norm.pdf(x, mu, np.sqrt(sigma_sq))
        plt.plot(x, y, color="black", label='Normal Distribution')
        plt.legend()
        plt.show()

        plt.hist(seq2y, bins=100, density=True, alpha=0.6, color='blue', label='Observed Distribution')
        plt.xlabel('X')
        plt.ylabel('Probability Density')
        plt.title(f'Frequency Distribution of Sampled Values (N({mu},{sigma_sq}), {n} samples) (Bray)')
        plt.legend()

        x = np.linspace(mu - 3*np.sqrt(sigma_sq), mu + 3*np.sqrt(sigma_sq), 1000)
        y = norm.pdf(x, mu, np.sqrt(sigma_sq))
        plt.plot(x, y, color="black", label='Normal Distribution')
        plt.legend()
        plt.show()


def box_muller(n):
    print("box_muller for n = " + str(n))
    z1 = list()
    start = time.time()
    for i in range(n):
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1)
        r = math.pow(-2*np.log(u1), 1/2)
        theta = 2*np.pi*u2
        t = r*np.sin(theta)
        z1.append(t)
    end = time.time()

    total_time = (end-start)**3
    print("computational time = " + str(total_time) + "ms")

    mean1 = np.mean(z1)
    var1 = np.var(z1)
    print("mean = " + str(mean1))
    print("variance = " + str(var1))
    print()
    plt.hist(z1, bins='auto', density=True, alpha=0.6, color='red')
    plt.xlabel('Sampled Values')
    plt.ylabel('Frequency')
    plt.title(f'Frequency Distribution of Sampled Values (Box-Muller, {n} samples)')
    plt.show()
    return z1


def bray(n):
    print("bray for n = " + str(n))
    z1 = list()
    start = time.time()
    count = 0
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
        count += 1
    end = time.time()
    total_time = (end-start)**3
    print("computational time = " + str(total_time) + "ms")

    print(f"Proportion rejected = {(count-n)/count}")
    print(f"1-\u03C0/4 = {1-np.pi/4}")
    print(f"Comparing with 1-\u03C0/4 => {((count-n)/count)/(1-np.pi/4)}")
    mean1 = np.mean(z1)
    var1 = np.var(z1)
    print("mean = " + str(mean1))
    print("variance = " + str(var1))
    print()
    plt.hist(z1, bins='auto', density=True, alpha=0.6, color='blue')
    plt.xlabel('Sampled Values')
    plt.ylabel('Frequency')
    plt.title(f'Frequency Distribution of Sampled Values (Bray, {n} samples)')
    plt.show()

    return z1


n_values = [100, 10000]
for n in n_values:
    N(n)

