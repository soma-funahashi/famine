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

fig, ax = plt.subplots()

dat = (a, b)

bp = ax.boxplot(dat, sym=".")

plt.show()