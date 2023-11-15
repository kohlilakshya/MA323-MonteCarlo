import numpy as np 
import matplotlib.pyplot as plt  
from collections import OrderedDict


#Answer 1
print("Answer 1")
def generator(a, b, m, x0):
    xi = list()
    xi.append(x0)
    while True:
        x0 = (a * x0 + b) % m
        if x0 in xi:
            #xi.append(x0) 
            #if we want repeating element to be in the list, uncomment
            break
        xi.append(x0)
    return xi

print("for a = 6, b = 0, m = 11:")
for i in range(0,11):
    sequence = generator(6,0,11,i)
    print("x0 =",i, "& Sequence = ", sequence)

print()

print("for a = 3, b = 0, m = 11:")
for i in range(0,11):
    sequence = generator(3,0,11,i)
    print("x0 = ",i, " & Sequence = ", sequence)


#Answer2
print("Answer 2")
def generator2(a, b, m, x0):
    ui = list()
    hashmap = dict()
    for i in range(0,20):
        hashmap[i]=0

    for i in range(0,10000):
        x0 = (a*x0 + b)%m
        u = x0/m
        ui.append(u)
        freq = round(u*20)%20
        hashmap[freq]+=1
    return hashmap

x0_values = [0,2,5,7,10]
a_values = [1597, 51749]
for i in range(0,2):
    print("for a = " + str(a_values[i]) + ", b = 1 , m = 244944:")
    for j in range(0,5):
        hashmap = generator2(a_values[i],1,244944,x0_values[j])
        hashmap = OrderedDict(sorted(hashmap.items())) 
        oldKeys = list(hashmap.keys())
        hashmap = dict((round(key*0.05, 2), value) for (key, value) in hashmap.items())

        x = list(hashmap.keys())
        y = list(hashmap.values())

        plt.figure(figsize=(18, 5))
        width = np.min(np.diff(oldKeys))/3
        plt.bar(oldKeys - 0.5*width, y, color='blue', width=0.3, ec='black', label='a = 1597') 
        print("Frequency table for x0 = ", x0_values[j])
        plt.xlabel("Ranges")
        plt.ylabel("Frequency")
        plt.title("Answer 2 - Value of seed(x0) = " +str(x0_values[j]) + ", a = " + str(a_values[i])+ ", b=1, m = 244944")

        print(hashmap)
        print()
        plt.savefig("q3 x0 = " + str(x0_values[j]) + ", a = " + str(a_values[i]))
        # plt.show()

#Answer 3
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
plt.scatter(ux,uy)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Answer 3: Two Dimensional plot")
plt.savefig("q3")
# plt.show()

