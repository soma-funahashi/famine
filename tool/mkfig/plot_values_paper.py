import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")
sns.set(style="ticks")
from matplotlib import rc
rc('mathtext', default='regular')



fam = pd.read_csv("../../dat/fam/famineData.csv")
fam_mean = fam.sum(axis = 1)
fig = plt.figure(figsize=(9,12))


def filename(fn):
    if fn == "aws":
        fin = "aws/mod2_SupAgr__WFDELECD.csv"
        lab = "Agricultural water input"
    if fn == "cor":
        fin = "cor/correlation_data.csv"
        lab = "Correlation coefficient b/w\nAWS and VAP (1961 - 2014)"
    elif fn == "gdp":
        fin = "gdp/gdp_per_cap_filled.csv"
        lab = "GDP per capita ($, ave. of 1961 - 2019)"
    elif fn == "upp":
        fin = "upp/upp_new_filled.csv"
        lab = "Urban population rate\n(%, ave. of 1961 - 2019)"
    elif fn == "gin":
        fin = "../dat/gin/gini_coeff_ave.csv"
        lab = "Gini Coefficient"
    elif fn == "war":
        fin = "../dat/war/war_prob.csv"
        lab = "War (freqquency, 1961 - 2019)"
    elif fn == "fpr":
        fin = "../dat/fpr/cereal_import_dependency.csv"
        lab = "Cereal import dependency\n(%, ave. of 2001 - 2016)"
    elif fn == "sow":
        fin = "../dat/sow/soilmois_cropland_kg_merged.csv"
        lab = r"Soil water ($kg/m^2$, ave. of 1961 - 2014)"

    return [fin, lab]


def plot_values(xdata, ydata, idx):
    ### input data
    xfn = filename(xdata)
    yfn = filename(ydata)
    df1 = pd.read_csv("../../dat/"+xfn[0])
    df2 = pd.read_csv("../../dat/"+yfn[0])
    ax = fig.add_subplot(3,2,idx)

    val1 = df1.mean(axis="columns")
    val2 = df2.mean(axis="columns")

    dat_0 = [[],[]]
    dat_1 = [[],[]]

    if xdata == "gdp":
        ax.set_xscale("log")
    
    for i in range(len(fam_mean)):
        if fam_mean[i] > 0:
            dat_1[0].append(val1[i])
            dat_1[1].append(val2[i])
        else:
            dat_0[0].append(val1[i])
            dat_0[1].append(val2[i])

    ax.scatter(dat_1[0], dat_1[1], color="red", alpha=0.5, zorder = 1, label = "Famine experienced countries")
    ax.scatter(dat_0[0], dat_0[1], color="gray", alpha=0.5, zorder = 0, label = "Other countries")
    
    ax.set_xlabel(xfn[1])
    ax.set_ylabel(yfn[1])

    titleChar = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}

    ax.set_title("2."+titleChar[idx], loc="left", fontweight='bold')

    if idx == 5:
        ax.legend(bbox_to_anchor=(2.5, 0.89), loc='right', borderaxespad=0, fontsize=12, ncol=1)

def main():
    plot_values("sow", "war", 1)
    plot_values("cor", "fpr", 2)
    plot_values("gdp", "fpr", 3)
    plot_values("gdp", "upp", 4)
    plot_values("gdp", "gin", 5)

    plt.subplots_adjust(wspace=0.5, hspace=0.7)
    plt.savefig("../../fig/plt/plot_paper.png", bbox_inches = "tight", dpi = 300)
    plt.show()


if __name__ == "__main__":
    main()