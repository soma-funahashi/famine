import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")
sns.set(style="ticks")

gdp = pd.read_csv("../../dat/fpi/gdp_per_cap_fpi.csv")
upp = pd.read_csv("../../dat/upp/upp_new_filled.csv")
cor = pd.read_csv("../../dat/cor/correlation_data.csv")
gin = pd.read_csv("../../dat/gin/gini_coeff_ave.csv")
gdp_mean = gdp.mean(axis = 1)
upp_mean = upp.mean(axis = 1)
cor_mean = cor.mean(axis = 1)
gin_mean = gin.mean(axis = 1)

fam = pd.read_csv("../../dat/fam/famineData.csv")
fam_mean = fam.sum(axis = 1)

fig, ax = plt.subplots(1, 2, figsize=(8,4))

print(gdp)

gdp_cor_0 = [[],[]]
gdp_cor_1 = [[],[]]
gin_upp_0 = [[],[]]
gin_upp_1 = [[],[]]

for i in range(len(fam_mean)):
    if cor_mean[i] == 1:
        continue
    if fam_mean[i] > 0:
        gdp_cor_1[0].append(gdp_mean[i])
        gdp_cor_1[1].append(cor_mean[i])
    else:
        gdp_cor_0[0].append(gdp_mean[i])
        gdp_cor_0[1].append(cor_mean[i])

for i in range(len(fam_mean)):
    if fam_mean[i] > 0:
        gin_upp_1[0].append(gin_mean[i])
        gin_upp_1[1].append(upp_mean[i])
    else:
        gin_upp_0[0].append(gin_mean[i])
        gin_upp_0[1].append(upp_mean[i])

ax[0].scatter(gdp_cor_1[0], gdp_cor_1[1], color="red", alpha=0.5, zorder = 1, label = "Famine experienced\ncountries")
ax[0].scatter(gdp_cor_0[0], gdp_cor_0[1], color="gray", alpha=0.5, zorder = 0, label = "Other countries")

ax[0].set_xlabel("GDP per capita (Ave. of 1961~2019)")
ax[0].set_ylabel("Correlation coefficient b/w AWI and VAP")

ax[1].scatter(gin_upp_1[0], gin_upp_1[1], color="red", alpha=0.5, zorder = 1, label = "Famine experienced\ncountries")
ax[1].scatter(gin_upp_0[0], gin_upp_0[1], color="gray", alpha=0.5, zorder = 0, label = "Other countries")

ax[1].set_xlabel("gini coefficient")
ax[1].set_ylabel("Urban poplulation rate (Ave. of 1961~2019)")

#plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc="left")
plt.legend(fontsize=10)

axs = plt.gcf().get_axes()

print(axs)
# 軸毎にループ
for ax in axs:
    plt.axes(ax)
    #plt.xscale("log")

fig.tight_layout()

#plt.savefig("../../fig/plt/scatter.png", bbox_inches = "tight", dpi = 300)
plt.show()
