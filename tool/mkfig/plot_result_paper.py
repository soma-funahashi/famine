import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")
sns.set(style="ticks")
from matplotlib import rc
rc('mathtext', default='regular')

lor = pd.read_csv("../../out/logisticRegression_all.csv", index_col="ISO3")
fam = pd.read_csv("../../dat/fam/famineData_all.csv", index_col="ISO3")

plt.figure(figsize=(8,6))
yl = np.arange(1961,2015).astype(int)
lor_val = lor.values

print(lor_val)

lab1 = True
lab2 = True
lab3 = True

for i in range(len(fam)):
    tmp = lor_val[i].astype("float32")
    dfs = fam.sum(axis=1)
    if dfs[i] == 0:
        if lab2:
            plt.plot(yl, tmp, linewidth=0.5, color="lightgray", label="Countries with famine")
            lab2 = False
        else:
            plt.plot(yl, tmp, linewidth=0.5, color="lightgray")
    else:
        if lab1:
            plt.plot(yl, tmp, linewidth=0.5, color="red", zorder=50, label="Countries without famine")
            lab1 = False
        else:
            plt.plot(yl, tmp, linewidth=0.5, color="red", zorder=50)


for y in range(1961,2015):
    for i in range(len(fam)):
        cnt = fam.index[i]
        if fam.loc[cnt, str(y)] != 0:
            print(y, cnt, lor_val[i][y - 1961])
            if lab3:
                plt.scatter(y, lor_val[i][y - 1961], color="Red", s=10, alpha=0.5, linewidths=None, zorder=100, label="Famine years")
                lab3 = False
            else:
                plt.scatter(y, lor_val[i][y - 1961], color="Red", s=10, alpha=0.5, linewidths=None, zorder=100)

plt.ylabel("Probability of famine")
plt.legend()
plt.savefig("../../fig/plt/result_paper.png", bbox_inches="tight", dpi=300)
plt.show()