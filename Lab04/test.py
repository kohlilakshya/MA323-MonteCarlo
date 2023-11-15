import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.linspace(-3,3, 1000)
print(x)

fx = norm.pdf(x)
plt.plot(x,fx)
plt.show()