###########################################################
#to          : plot two data
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2020/02/25
###########################################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")
sns.set(style="ticks")

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
        fin = "upp/upp_new_filled.csv"
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
    elif fn == "uppf":
        fin = "../dat/upp/upp_future.csv"
        lab = "Urban population (Future)"
    elif fn == "imp":
        fin = "../dat/gdp/import_inp_filled.csv"
        lab = "Imported Value / GDP (%)"
    elif fn == "imppc":
        fin = "../dat/gdp/imported_value_per_cap.csv"
        lab = "Imported Value per capita (current USD)"
    elif fn == "gin":
        fin = "../dat/gin/gini_coeff_ave.csv"
        lab = "Gini Coefficient"

    return [fin, lab]

### edit here   #select from aws, cor, gdp, pop, unr, upp, vap
xdata = "gdp"
ydata = "cor"
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
df3 = pd.read_csv("../../out/"+prj+"____rslt.csv")
df4 = pd.read_csv("../../dat/fam/famineData_drought.csv")
val3 = df3.values
val4 = df4.values
tmp3 = []
tmp4 = []

for i in range(len(df3)):
    mx = 0
    for j in range(1, df3.shape[1]):
        mx = max(val3[i][j], mx)
    tmp3.append(mx)
    mx = 0
    for j in range(1, df4.shape[1]):
        mx = max(val4[i][j], mx)
    tmp4.append(mx)


### plotting
plt.figure(figsize=(7,6))
#plt.scatter(tmp1, tmp2, color="black", alpha=0.3, edgecolor=None)

for i in range(len(df3)):
    if tmp3[i] == 3 and tmp4[i] == 1:
#       plt.scatter(tmp1[i],tmp2[i], color="purple", alpha=0.5, edgecolor=None)
        plt.scatter(tmp1[i],tmp2[i], color="red", alpha=0.5, edgecolor=None)
        #plt.text(tmp1[i], tmp2[i], df1["ISO3"][i], color="red")
        print(df1["ISO3"][i], tmp1[i], tmp2[i])
    elif tmp3[i] == 3 and tmp4[i] != 1:
#       plt.scatter(tmp1[i],tmp2[i], color="blue", alpha=0.5, edgecolor=None)
        plt.scatter(tmp1[i],tmp2[i], color="black", alpha=0.5, edgecolor=None)
    elif tmp3[i] != 3 and tmp4[i] == 1:
        plt.scatter(tmp1[i],tmp2[i], color="red", alpha=0.5, edgecolor=None)
        #plt.text(tmp1[i], tmp2[i], df1["ISO3"][i], color="red")
        print(df1["ISO3"][i], tmp1[i], tmp2[i])
    elif tmp3[i] != 3 and tmp4[i] != 1:
        plt.scatter(tmp1[i],tmp2[i], color="black", alpha=0.5, edgecolor=None)


# for i in range(len(val)):
#     if val[i] == "n":
#         plt.scatter(tmp1[i],tmp2[i], color="black", alpha=0.3, edgecolor=None)
#     elif val[i] == "m":
#         plt.scatter(tmp1[i],tmp2[i], color="black", alpha=0.3, edgecolor=None)
# #       plt.scatter(tmp1[i],tmp2[i], color="tomato", alpha=0.3, edgecolor=None)
#     elif val[i] == "o":
#         plt.scatter(tmp1[i],tmp2[i], color="brack", alpha=0.3, edgecolor=None)
#         print(df3["ISO3"][i],tmp1[i],tmp2[i])
# #       plt.scatter(tmp1[i],tmp2[i], color="royalblue", alpha=0.3, edgecolor=None)
#     else:
#         plt.scatter(tmp1[i],tmp2[i], color="black", alpha=0.3, edgecolor=None)
#         print(df3["ISO3"][i],np.round(tmp1[i],3),np.round(tmp2[i],3))


if logscale:
    plt.xscale("log")

plt.xlim(100,)
plt.xlabel(xfn[1])
plt.ylabel(yfn[1])
plt.savefig("../../fig/plt/"+prj+"____"+xdata+"_"+ydata+".png")
plt.show()
