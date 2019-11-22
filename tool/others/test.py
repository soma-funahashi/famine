import numpy as np


def hamako(array):
    out = [np.max(array), np.min(array), np.median(array)]
    return out

a = np.arange(10)

print("list   :", hamako(a))
print("median :", hamako(a)[2]) ### print median of the array
