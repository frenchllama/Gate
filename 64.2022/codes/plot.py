import numpy as np
import matplotlib.pyplot as plt

V=[]

with open('vals.txt', 'r') as file:
    decimal_values = [float(line) for line in file.readlines()]

for value in decimal_values:
    V.append(value)

Xpdf = np.linspace(-2, 1, 100)
Ypdf, Ycdf = [], []

for i in Xpdf:
    if i<0:
        Ypdf.append(0.25*i + 0.5)
        Ycdf.append(0.125*(i+2)*(i+2))
    else:
        Ypdf.append(0.5)
        Ycdf.append(0.5*(i+1))



binNum = 100

PDF = np.histogram(V, bins=binNum, density=True)[0]
Vals = np.histogram(V, bins=binNum)[1][:-1]
CDF = np.cumsum(PDF)*((Vals[-1]-Vals[0])/binNum)

plt.figure(figsize=(8,8)) 

plt.subplot(221)
plt.plot(Vals, PDF)
plt.xlabel('x')
plt.ylabel('PDF simulated')

plt.subplot(222)
plt.plot(Xpdf, Ypdf)
plt.xlabel('x')
plt.ylabel('PDF actual')

plt.subplot(223)
plt.plot(Vals, CDF)
plt.xlabel('x')
plt.ylabel('CDF simulated')

plt.subplot(224)
plt.plot(Xpdf, Ycdf)
plt.xlabel('x')
plt.ylabel('CDF actual')

plt.savefig("../figs/z.png", bbox_inches='tight')

plt.show()