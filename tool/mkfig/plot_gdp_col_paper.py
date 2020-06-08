import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")
sns.set(style="ticks")

gdp = pd.read_csv("../../dat/gdp/gdp_per_cap_filled.csv")
cor = pd.read_csv("../../dat/cor/correlation_data.csv")
gdp_mean = gdp.mean(axis = 1)
cor_mean = cor.mean(axis = 1)

fam = pd.read_csv("../../dat/fam/famineData.csv")
fam_mean = fam.sum(axis = 1)

plt.figure(figsize=(7,6))
plt.xscale("log")

for i in range(len(fam_mean)):
    if cor_mean[i] == 1:
        continue
    if fam_mean[i] > 0:
        plt.scatter(gdp_mean[i], cor_mean[i], color="red", alpha=0.5, zorder = 1)
        plt.text(gdp_mean[i] + 10, cor_mean[i] + 0.01, fam["ISO3"][i], color="red", fontsize = 8)
    else:
        plt.scatter(gdp_mean[i], cor_mean[i], color="gray", alpha=0.5, zorder = 0)

plt.xlim(100,)

plt.show()