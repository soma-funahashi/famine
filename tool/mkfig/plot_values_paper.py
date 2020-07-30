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
    elif fn == "war":
        fin = "../dat/war/war.csv"
        lab = "War"
    elif fn == "warp":
        fin = "../dat/war/war_prob.csv"
        lab = "War (occurence probability)"
    elif fn == "fpr":
        fin = "../dat/fpr/cereal_import_dependency.csv"
        lab = "Cereal import dependency (%, 2001-2016)"
    elif fn == "vap":
        fin = "../dat/vap/vap_per_capita.csv"
        lab = "Value of Agricultural Production"
    elif fn == "vappc":
        fin = "vap/vap_per_capita.csv"
        lab = "Value of Agricultural Production per capita (Int.100$/year)"
    elif fn == "sow":
        fin = "../dat/sow/soilmois_cropland_kg_merged.csv"
        lab = "Soil water (kg/m2)"
    elif fn == "lor":
        fin = "../out/logisticRegression_all.csv"
        lab = "Logistic Regression"

    return [fin, lab]

fam = pd.read_csv("../../dat/fam/famineData.csv")
fam_mean = fam.sum(axis = 1)

fig, ax = plt.subplots(1, 1, figsize=(5,5))

def plot_values(xdata, ydata):
    ### input data
    xfn = filename(xdata)
    yfn = filename(ydata)
    df1 = pd.read_csv("../../dat/"+xfn[0])
    df2 = pd.read_csv("../../dat/"+yfn[0])

    val1 = df1.mean(axis="columns")
    val2 = df2.mean(axis="columns")

    dat_0 = [[],[]]
    dat_1 = [[],[]]

    for i in range(len(fam_mean)):
        if fam_mean[i] > 0:
            dat_1[0].append(val1[i])
            dat_1[1].append(val2[i])
        else:
            dat_0[0].append(val1[i])
            dat_0[1].append(val2[i])
    ax.scatter(dat_1[0], dat_1[1], color="red", alpha=0.5, zorder = 1, label = "Famine experienced\ncountries")
    ax.scatter(dat_0[0], dat_0[1], color="gray", alpha=0.5, zorder = 0, label = "Other countries")
    
    ax.set_xlabel(xfn[1])
    ax.set_ylabel(yfn[1])

    plt.xscale("log")

    plt.legend(fontsize=10)
    plt.savefig("../../fig/plt/plot_"+xdata+"_"+ydata+"_paper.png", bbox_inches = "tight", dpi = 300)
    plt.show()

plot_values("gdp", "gin")