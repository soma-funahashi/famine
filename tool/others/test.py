import numpy as np


def hamako(array):
    out = [np.max(array), np.min(array), np.median(array)]
    return out

a = np.arange(10)

print("list   :", hamako(a))
print("median :", hamako(a)[2]) ### print median of the array


import matplotlib.pyplot as plt

plt.figure()
a = np.arange(10)
b = np.arange(10)
plt.plot(a,b)
plt.show()