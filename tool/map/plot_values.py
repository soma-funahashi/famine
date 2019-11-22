###########################################################
#to          : draw a gif animation of model output
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/10/15
###########################################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def filename(fn):
    if fn == "aws":
        fin = "aws/mod2_SupAgr__WFDELECD.csv"
        lab = "Agricultural water input"
    elif fn == "cor":
        fin = "cor/correlation.csv"
        lab = "Correlation"
    elif fn == "gdp":
        fin = "gdp/gdp_per_cap.csv"
        lab = "GDP per capita"
    elif fn == "upp":
        fin = "upp/urban_population.csv"
        lab = "Urban population rate"
    elif fn == "unr":
        fin = "unr/undernourishment.csv"
        lab = "Undernourished population rate"
    
    return [fin, lab]

### edit here   #select from aws, cor, gdp, pop, unr, upp, vap
xdata = "gdp"
ydata = "upp"
logscale = True

### input data
xfn = filename(xdata)
yfn = filename(ydata)
df1 = pd.read_csv("../../dat/"+xfn[0])
df2 = pd.read_csv("../../dat/"+yfn[0])

tmp1 = []
tmp2 = []

tmp1 = df1.mean(axis="columns")
tmp2 = df2.mean(axis="columns")

### model output
prj = "dflt"
df3 = pd.read_csv("../../out/"+prj+"____vald.csv")
val = df3["Result"]

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

if logscale:
    plt.xscale("log")

plt.xlabel(xfn[1])
plt.ylabel(yfn[1])
plt.savefig("../../fig/plt/"+prj+"____"+xdata+"_"+ydata+".png")
plt.show()
