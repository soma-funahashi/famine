###########################################################
#to          : plot two data
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/11/29
###########################################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def filename(fn):
    if fn == "aws":
        fin = "aws/mod2_SupAgr__WFDELECD.csv"
        lab = "Agricultural water input"
    elif fn == "cor":
        fin = "cor/correlation_data.csv"
        lab = "Correlation b/w AWS and VAP"
    elif fn == "gdp":
        fin = "gdp/gdp_per_cap_filled.csv"
        lab = "GDP per capita"
    elif fn == "gpi":
        fin = "gpi/global_peace_index.csv"
        lab = "Global Peace Index"
    elif fn == "upp":
        fin = "upp/urban_population.csv"
        lab = "Urban population rate"
    elif fn == "unr":
        fin = "unr/undernourishment.csv"
        lab = "Undernourished population rate"
    elif fn == "awspc":
        fin = "aws/aws_per_capita.csv"
        lab = "AWS per capita"
    elif fn == "mrg":
        fin = "../out/multiRegression.csv"
        lab = "Famine Vulnerability"

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
        plt.scatter(tmp1[i],tmp2[i], color="black", alpha=0.3, edgecolor=None)
#       plt.scatter(tmp1[i],tmp2[i], color="tomato", alpha=0.3, edgecolor=None)
    elif val[i] == "o":
        plt.scatter(tmp1[i],tmp2[i], color="red", alpha=0.3, edgecolor=None)
        print(df3["ISO3"][i],tmp1[i],tmp2[i])
#       plt.scatter(tmp1[i],tmp2[i], color="royalblue", alpha=0.3, edgecolor=None)
    else:
        plt.scatter(tmp1[i],tmp2[i], color="red", alpha=0.3, edgecolor=None)
        print(df3["ISO3"][i],np.round(tmp1[i],3),np.round(tmp2[i],3))

if logscale:
    plt.xscale("log")

plt.xlabel(xfn[1])
plt.ylabel(yfn[1])
plt.savefig("../../fig/plt/"+prj+"____"+xdata+"_"+ydata+".png")
plt.show()
