import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

inp = pd.read_csv("../../out/logisticRegression_all.csv")
fam = pd.read_csv("../../dat/fam/famineData_all.csv")

a = []
b = []

for y in range(1961, 2015):
    for i in range(len(inp)):
        if fam[str(y)][i] > 0:
            a.append(inp[str(y)][i])
        else:
            b.append(inp[str(y)][i])

	
plt.hist([a, b], stacked=True, color = ["red", "gray"], bins = 40, range=(0.04,1))
#plt.yscale("log")

plt.savefig("../../fig/hist/hist_all.png")
plt.show()