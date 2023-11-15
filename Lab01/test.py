import numpy as np
import matplotlib.pyplot as plt

print("Answer 3")
def generator3(a, b, m, x0):
    ui = list()
    for i in range(0,10000):
        x0 = (a*x0 + b)%m
        ui.append(x0/m)
    return ui

print("for a = 1229, b = 1, m = 2048:")
# ux = x coordinate & uy = y coordinate 
ux = generator3(1229,1,2048,5)
uy = generator3(1229,1,2048,5)

del ux[len(ux)-1]
del uy[0]

# ax = axis. fig = figure
# fig, ax = plt.subplots()
# ax.scatter(ux, uy)
plt.scatter(ux, uy)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Answer 3: Two Dimensional plot")
plt.show()

