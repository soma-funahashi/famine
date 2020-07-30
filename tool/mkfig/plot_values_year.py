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
        fin = "cor/correlation_data_year.csv"
        lab = "Correlation b/w AWS and VAP"
    elif fn == "gdp":
        fin = "fpi/gdp_per_cap_fpi.csv"
#       fin = "fpi/gdp_per_cap_fpi_5yrs_min.csv"
        lab = "GDP per capita (food price considered)"
    elif fn == "gpi":
        fin = "gpi/global_peace_index.csv"
        lab = "Global Peace Index"
    elif fn == "upp":
        fin = "upp/upp_new_filled.csv"
#       fin = "upp/upp_5yrs_min.csv"
        lab = "Urban population rate"
    elif fn == "unr":
        fin = "unr/undernourishment.csv"
        lab = "Undernourished population rate"
    elif fn == "awspc":
        fin = "aws/aws_per_capita.csv"
        lab = "AWS per capita"
    elif fn == "vappc":
        fin = "vap/vap_per_capita.csv"
        lab = "Value of Agricultural Production per capita (Int.100$/year)"
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
#       fin = "../dat/war/war_5yrs_max.csv"
        lab = "War"
    elif fn == "warwma":
        fin = "../dat/war/war_wma.csv"
        lab = "War (weighted moving average of 5 years)"
    elif fn == "sow":
        fin = "../dat/sow/soilmois_cropland_ave_hist.csv"
        lab = "Soil Moisture"
    elif fn == "csp":
        fin = "../dat/csp/domestic_production_consumed.csv"
        lab = "Domestic production consumed per capita (100$, 1961-2016)"
    elif fn == "pdi":
        fin = "../dat/pdi/mod3_pdsi.csv"
        lab = "Palmer's Drought Severity Index (1961 - 2018)"

    return [fin, lab]

fam = pd.read_csv("../../dat/fam/famineData.csv")
#fam = pd.read_csv("../../dat/fam/fam_5yrs_max.csv")

xdata = "pdi"
ydata = "war"
logscale = False
saveflag = False

xfn = filename(xdata)
yfn = filename(ydata)
inp_x = pd.read_csv("../../dat/"+xfn[0])
inp_y = pd.read_csv("../../dat/"+yfn[0])

dat_0 = [[],[]]
dat_1 = [[],[]]

#year = np.arange(1961, 2015)
year = np.arange(1971, 2005)
#year = np.arange(1961, 2016, 5)

for yr in year:
    yr = str(yr)
    for i in range(len(fam)):
        if fam[yr][i] == 1:
            dat_1[0].append(inp_x[yr][i])
            dat_1[1].append(inp_y[yr][i])
            print(yr, fam["ISO3"][i], inp_x[yr][i], inp_y[yr][i])
        else:
            dat_0[0].append(inp_x[yr][i])
            dat_0[1].append(inp_y[yr][i])

plt.scatter(dat_1[0], dat_1[1], color="red", alpha=0.5, zorder = 1, label = "Famine years")
plt.scatter(dat_0[0], dat_0[1], color="gray", alpha=0.5, zorder = 0, label = "Other years")

plt.legend(fontsize=10)

if logscale:
    plt.xscale("log")

plt.xlabel(xfn[1])
plt.ylabel(yfn[1])
plt.tight_layout()

if saveflag:
    plt.savefig("../../fig/plt/"+xdata+"_"+ydata+"_year.png")

plt.show()