import numpy as np
import pandas as pd
from scipy import stats

## READING NECESSARY DATASET

#### Hazard
sow = pd.read_csv("../dat/sow/soilmois_cropland_kg_merged_st.csv", index_col="ISO3")
war = pd.read_csv("../dat/war/war_prob_st.csv", index_col="ISO3")
# sow = pd.read_csv("../dat/pdi/mod3_pdsi.csv", index_col="ISO3")

#### Exposure
cor = pd.read_csv("../dat/cor/correlation_data_st.csv", index_col="ISO3")
fpr = pd.read_csv("../dat/fpr/fpr_st.csv", index_col="ISO3")

#### Vulnerability
gdp = pd.read_csv("../dat/gdp/gdp_per_cap_log_st.csv", index_col="ISO3")
upp = pd.read_csv("../dat/upp/upp_st.csv", index_col="ISO3")
gin = pd.read_csv("../dat/gin/gini_coeff_ave_st.csv", index_col="ISO3")
# gdp = pd.read_csv("../dat/fpi/gdp_per_cap_fpi.csv", index_col="ISO3")
# gdp = pd.read_csv("../dat/gdp/gdp_per_cap_st.csv", index_col="ISO3")
# upp = pd.read_csv("../dat/upp/upp_new_filled.csv", index_col="ISO3")
upp = upp.fillna(upp.mean())
gin = gin.fillna(gin.mean())

#### famine
fam = pd.read_csv("../dat/fam/famineData_around.csv", index_col="ISO3")



## FUNCTION

def prep():
    sow_list = []
    war_list = []
    cor_list = []
    fpr_list = []
    gdp_list = []
    upp_list = []
    gin_list = []
    fam_list = []
    for i in range(len(gdp)):
        for yr in range(1961, 2015):
            sow_list.append(sow.iat[i, yr - 1961])
            war_list.append(war.iat[i, 0])
            cor_list.append(cor.iat[i, 0])
            fpr_list.append(fpr.iat[i, 0])
            gdp_list.append(gdp.iat[i, yr - 1960])
            upp_list.append(upp.iat[i, yr - 1960])
            gin_list.append(gin.iat[i, 0])
            fam_list.append(fam.iat[i, yr - 1961])
    X = pd.DataFrame()
    Y = pd.DataFrame()
    X["sow"] = sow_list
    X["war"] = war_list
    X["cor"] = cor_list
    X["fpr"] = fpr_list
    X["gdp"] = gdp_list
    X["upp"] = upp_list
    X["gin"] = gin_list
    Y["fam"] = fam_list
    return X, Y


def calc(dat):
    X, Y = prep()
    famineCase = []
    nonFamineCase = []
    for i in range(len(X[dat])):
        if Y["fam"][i] == 1:
            famineCase.append(X[dat][i])
        else:
            nonFamineCase.append(X[dat][i])
    res = stats.mannwhitneyu(famineCase, nonFamineCase, alternative='two-sided')
    print(dat, res.pvalue)


def main():
    val_list = ["sow", "war", "cor", "fpr", "gdp", "upp", "gin"]
    for val in val_list:
        calc(val)


if __name__ == "__main__":
    main()