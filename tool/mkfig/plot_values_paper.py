import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")
sns.set(style="ticks")
from matplotlib import rc
rc('mathtext', default='regular')

def filename(fn):
    if fn == "aws":
        fin = "aws/mod2_SupAgr__WFDELECD.csv"
        lab = "Agricultural water input"
    if fn == "cor":
        fin = "cor/correlation_data.csv"
        lab = "Correlation coefficient b/w\nAWS and VAP (1961-2014)"
    elif fn == "gdp":
        fin = "gdp/gdp_per_cap_filled.csv"
        lab = "GDP per capita ($, 1961-2019)"
    elif fn == "upp":
        fin = "upp/upp_new_filled.csv"
        lab = "Urban population rate"
    elif fn == "gin":
        fin = "../dat/gin/gini_coeff_ave.csv"
        lab = "Gini Coefficient"
    elif fn == "war":
        fin = "../dat/war/war_prob.csv"
        lab = "War (freqquency, 1961-2019)"
    elif fn == "fpr":
        fin = "../dat/fpr/cereal_import_dependency.csv"
        lab = "Cereal import dependency\n(%, 2001-2016)"
    elif fn == "vap":
        fin = "../dat/vap/vap_per_capita.csv"
        lab = "Value of Agricultural Production"
    elif fn == "sow":
        fin = "../dat/sow/soilmois_cropland_kg_merged.csv"
        lab = r"Soil water $(kg/m^2, 1961-2014)$"


    return [fin, lab]

fam = pd.read_csv("../../dat/fam/famineData.csv")
fam_mean = fam.sum(axis = 1)

fig, ax = plt.subplots(3, 2, figsize=(9,12))

def plot_values(xdata, ydata, xpos, ypos):
    ### input data
    xfn = filename(xdata)
    yfn = filename(ydata)
    df1 = pd.read_csv("../../dat/"+xfn[0])
    df2 = pd.read_csv("../../dat/"+yfn[0])

    val1 = df1.mean(axis="columns")
    val2 = df2.mean(axis="columns")

    dat_0 = [[],[]]
    dat_1 = [[],[]]

    if xdata == "gdp":
        ax[ypos][xpos].set_xscale("log")
    
    for i in range(len(fam_mean)):
        if fam_mean[i] > 0:
            dat_1[0].append(val1[i])
            dat_1[1].append(val2[i])
        else:
            dat_0[0].append(val1[i])
            dat_0[1].append(val2[i])

    ax[ypos][xpos].scatter(dat_1[0], dat_1[1], color="red", alpha=0.5, zorder = 1, label = "Famine experienced countries")
    ax[ypos][xpos].scatter(dat_0[0], dat_0[1], color="gray", alpha=0.5, zorder = 0, label = "Other countries")
    
    ax[ypos][xpos].set_xlabel(xfn[1])
    ax[ypos][xpos].set_ylabel(yfn[1])

    if xpos == 0 and ypos == 2:
        ax[ypos][xpos].legend(bbox_to_anchor=(1.1, 0), loc='lower right', borderaxespad=0, fontsize=14, ncol=2)

plot_values("sow", "war", 0, 0)
plot_values("cor", "fpr", 0, 1)
plot_values("gdp", "fpr", 1, 0)
plot_values("gdp", "upp", 1, 1)
plot_values("gdp", "gin", 0, 2)

plt.subplots_adjust(wspace=0.5, hspace=0.5)
#plt.savefig("../../fig/plt/plot_"+xdata+"_"+ydata+"_paper.png", bbox_inches = "tight", dpi = 300)
plt.show()