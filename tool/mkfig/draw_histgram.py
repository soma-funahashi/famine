import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../out/logisticRegression_guc.csv")
df = df.mean(axis = 1)
df = df.values
fam = pd.read_csv("../../dat/fam/famineData_drought.csv")
fam = fam.sum(axis=1)

tmp1 = []
tmp2 = []

for i in range(len(df)):
    if fam[i] > 0:
        tmp1.append(df[i])
    else:
        tmp2.append(df[i])

plt.hist(tmp2, color = "gray")
plt.hist(tmp1, color = "red", stacked = True)

plt.savefig("../../fig/hist/hist_guc.png")
plt.show()