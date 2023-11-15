import numpy as np
import matplotlib.pyplot as plt
import cmath
import math
from numpy import random

# Answer1
print("Answer 1")
def fx(i):
  return 20*i*math.pow(1 - i, 3)

def CDFx(i):
  return 10*i*i - 20*math.pow(i, 3) + 15*math.pow(i, 4) - 4*math.pow(i, 5)

c_values = [max(fx(i) for i in np.linspace(0,1,10000)), 5, 10]
for c in c_values:
  print("for c = "+ str(c))
  sequence = list()
  count = 0
  num_iter = list()
  while len(sequence) < 10000:
      X = np.random.uniform(0,1)
      U = np.random.uniform(0,1)
      index = 0
      count+=1
      if(U <= fx(X) / c):
          sequence.append(X)
          num_iter.append(count)
          count = 0

  # b
  actual_mean = 1/3
  sample_mean = np.mean(sequence)
  print("(b) Sample Mean: "+str(sample_mean))
  print("Actual Mean: " + str(actual_mean))
  
  # 
  in_range = sum(1 for x in sequence if 0.25<=x<=0.75)
  apx_probab = in_range/10000
  print("(c) Approximate value of P(0.25<=X<=0.75) = " + str(apx_probab))
  print("Exact value of P(0.25<=X<=0.75) = " + str(CDFx(0.75)-CDFx(0.25)))
  
  # d
  average_iterations = sum(num_iter)/len(num_iter)
  # print("Number of iterations")
  # print(num_iter)
  print("(d) Average of count of number of iterations "+str(average_iterations))
  print("Average number of iterations (part a) "+str(c))
  
  # e 
  x_vals = np.linspace(0, 1, 1000)
  plt.hist(sequence, bins=30, density=True, alpha=0.7, color='blue', label='Generated Samples')
  plt.plot(x_vals, [fx(x) for x in x_vals], color='red', label='Target Distribution')
  plt.xlabel('x')
  plt.ylabel('Probability Density')
  plt.title('Acceptance-Rejection Method (c = ' + str(c) + ')')
  plt.legend()
  plt.show()
  # plt.savefig(str(c))
  print()



# Answer 2
print("Answer 2")
def f2x(i, alpha):
    return np.power(i, alpha-1)*math.exp(-i)/math.gamma(alpha)

def gx(i, alpha):
    A = (1/alpha) + math.exp(-1)
    return math.pow(i, alpha-1)/A

alpha_val = [0.9]

for alpha in alpha_val:
    A = (1/alpha) + math.exp(-1)
    c = A/math.gamma(alpha)
    print("The rejection constant for alpha = " + str(alpha) + " is " + str(c))
    print()
    print("The dominating PDF is g(x) = (x^(alpha-1))/A, where A = (1/alpha) + (1/e)" )
    sequence = list()
    while len(sequence) < 10000:
        U1 = np.random.uniform(0,1)
        if(U1>1/(alpha*A)):
            continue
        X = math.pow(alpha*A*U1, 1/alpha)
        U2 = np.random.uniform(0,1)
        if c*gx(X, alpha)*U2 <= f2x(X, alpha) :
            sequence.append(X)
    x_vals = np.linspace(0, 1, 1000)
    plt.hist(sequence, bins=30, density=True, alpha=0.7, color='blue', label='Generated Samples')
    plt.plot(x_vals, [f2x(x, alpha) for x in x_vals], color='red', label='Target Distribution')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.title('Acceptance-Rejection Method (c = ' + str(c) + ')')
    plt.legend()
    plt.show()
    