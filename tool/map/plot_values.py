###########################################################
#to          : draw a gif animation of model output
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/10/15
###########################################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### input data
#df1 = pd.read_csv("../../dat/gdp_per_cap.csv")
#df2 = pd.read_csv("../../dat/urban_population.csv")

#df1 = pd.read_csv("../../dat/gdp_per_cap.csv")
#df2 = pd.read_csv("../../dat/correlation.csv")

#df1 = pd.read_csv("../../dat/urban_population.csv")
#df2 = pd.read_csv("../../dat/correlation.csv")

df1 = pd.read_csv("../../dat/urban_population.csv")
df2 = pd.read_csv("../../dat/undernourishment.csv")

tmp1 = []
tmp2 = []

tmp1 = df1.mean(axis="columns")
tmp2 = df2.mean(axis="columns")

### model output
prj = "dflt"
df3 = pd.read_csv("../../out/"+prj+"____vald.csv")

val = df3["Result"]
print(val[3])

### plotting

plt.figure()

for i in range(len(val)):
    if val[i] == "n":
        plt.scatter(tmp1[i],tmp2[i], color="black", alpha=0.3, edgecolor=None)
    elif val[i] == "m":
        plt.scatter(tmp1[i],tmp2[i], color="tomato", alpha=0.3, edgecolor=None)
    elif val[i] == "o":
        plt.scatter(tmp1[i],tmp2[i], color="royalblue", alpha=0.3, edgecolor=None)
    else:
        plt.scatter(tmp1[i],tmp2[i], color="darkorchid", alpha=0.3, edgecolor=None)

#plt.xscale("log")
#plt.xlabel("GDP per cap.")
#plt.ylabel("Urban population rate")
#plt.ylabel("correlation")
#plt.legend()

plt.show()
