import numpy as np
import matplotlib.pyplot as plt

V=[]

with open('vals.txt', 'r') as file:
    decimal_values = [float(line) for line in file.readlines()]

for value in decimal_values:
    V.append(value)

binNum = 100

PDF = np.histogram(V, bins=binNum, density=True)[0]
Vals = np.histogram(V, bins=binNum)[1][:-1]
CDF = np.cumsum(PDF)*((Vals[-1]-Vals[0])/binNum)

plt.figure(figsize=(8,8)) 

plt.subplot(211)
plt.plot(Vals, PDF)
plt.xlabel('x')
plt.ylabel('PDF')


plt.subplot(212)
plt.plot(Vals, CDF)
plt.xlabel('x')
plt.ylabel('CDF')

plt.savefig("../figs/z.png", bbox_inches='tight')

plt.show()