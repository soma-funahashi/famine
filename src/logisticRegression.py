import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve
import seaborn as sns
sns.set_style("whitegrid")

### Hazard
sow = pd.read_csv("../dat/sow/soilmois_cropland_kg_merged_st.csv", index_col="ISO3")
war = pd.read_csv("../dat/war/war_prob_st.csv", index_col="ISO3")
# sow = pd.read_csv("../dat/pdi/mod3_pdsi.csv", index_col="ISO3")

### Exposure
cor = pd.read_csv("../dat/cor/correlation_data_st.csv", index_col="ISO3")
fpr = pd.read_csv("../dat/fpr/fpr_st.csv", index_col="ISO3")

### Vulnerability
gdp = pd.read_csv("../dat/gdp/gdp_per_cap_log_st.csv", index_col="ISO3")
upp = pd.read_csv("../dat/upp/upp_st.csv", index_col="ISO3")
gin = pd.read_csv("../dat/gin/gini_coeff_ave_st.csv", index_col="ISO3")
# gdp = pd.read_csv("../dat/fpi/gdp_per_cap_fpi.csv", index_col="ISO3")
# gdp = pd.read_csv("../dat/gdp/gdp_per_cap_st.csv", index_col="ISO3")
# upp = pd.read_csv("../dat/upp/upp_new_filled.csv", index_col="ISO3")
upp = upp.fillna(upp.mean())
gin = gin.fillna(gin.mean())

### famine
fam = pd.read_csv("../dat/fam/famineData_around.csv", index_col="ISO3")


def main(ssp, rcp):
    sow_list = []
    war_list = []
    cor_list = []
    fpr_list = []
    gdp_list = []
    upp_list = []
    gin_list = []
    fam_list = []

    cnt = 0

    for i in range(len(gdp)):
        for yr in range(1961,2015):
            sow_list.append(sow.iat[i, yr - 1961])
            war_list.append(war.iat[i, 0])

            cor_list.append(cor.iat[i, 0])
            fpr_list.append(fpr.iat[i, 0])

            gdp_list.append(gdp.iat[i, yr - 1960])
            upp_list.append(upp.iat[i, yr - 1960])
            gin_list.append(gin.iat[i, 0])
            
            fam_list.append(fam.iat[i, yr - 1961])
            
            cnt += 1

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

    vals = "all"
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
    lr = LogisticRegression()
    lr.fit(X_train, Y_train)

    Y_pred = lr.predict(X_test)

    print("coefficient = ", lr.coef_)
    print("intercept = ", lr.intercept_)
    probs = lr.predict_proba(X)

    tmp = []
    for i in range(len(probs)):
        tmp.append(probs[i][1])
    tmp = np.array(tmp)
    tmp = tmp.reshape([162, 54])

    out = pd.DataFrame(index = gdp.index)
    for yr in range(1961, 2015):
        tmp2 = []
        for i in range(len(gdp)):
            tmp2.append(tmp[i][yr-1961])

        out[str(yr)] = tmp2
    out.to_csv("../out/logisticRegression_" + vals + ".csv")

    X_future = pd.DataFrame()
    gdp_f = pd.read_csv("../dat/gdp/gdp_per_cap_"+ssp+"_log_st.csv", index_col="ISO3")
    upp_f = pd.read_csv("../dat/upp/upp_future_st.csv", index_col="ISO3")
    sow_f = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp"+rcp+"_st.csv", index_col="ISO3")
    # gdp_f = pd.read_csv("../dat/gdp/gdp_per_cap_"+ssp+"_st.csv", index_col="ISO3")
    # gdp_f = pd.read_csv("../dat/gdp/gdp_per_cap_"+ssp+".csv", index_col="ISO3")
    # upp_f = pd.read_csv("../dat/upp/upp_future.csv", index_col="ISO3")
    # sow_f = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp"+rcp+".csv", index_col="ISO3")

    gdp_f = gdp_f.fillna(gdp_f.mean(axis = 0))

    sow_list_future = []
    war_list_future = []
    cor_list_future = []
    fpr_list_future = []
    gdp_list_future = []
    upp_list_future = []
    gin_list_future = []

    num = 0

    for i in range(len(gdp)):
        for yr in range(2021, 2051):
            sow_list_future.append(sow_f.iat[i, yr - 2021])
            war_list_future.append(war.iat[i, 0])
            cor_list_future.append(cor.iat[i, 0])    
            fpr_list_future.append(fpr.iat[i, 0])
            gdp_list_future.append(gdp_f.iat[i, yr - 2021])
            upp_list_future.append(upp_f.iat[i, yr - 2021])
            gin_list_future.append(gin.iat[i, 0])

    X_future["sow"] = sow_list_future
    X_future["war"] = war_list_future
    X_future["cor"] = cor_list_future
    X_future["fpr"] = fpr_list_future
    X_future["gdp"] = gdp_list_future
    X_future["upp"] = upp_list_future
    X_future["gin"] = gin_list_future

    probs_future = lr.predict_proba(X_future)

    tmp_f = []
    for i in range(162*30):
        tmp_f.append(probs_future[i][1])
    tmp_f = np.array(tmp_f)
    tmp_f = tmp_f.reshape([162, 30])

#   print("shape =", tmp_f.shape)

    out_f = pd.DataFrame(index = gdp.index)
    for yr in range(2021, 2051):
        tmp2_f = []
        for i in range(len(gdp)):
            tmp2_f.append(tmp_f[i][yr-2021])

        out_f[str(yr)] = tmp2_f
    out_f.to_csv("../out/logisticRegression_" + vals + "_future_"+ssp+"_rcp"+rcp+".csv")
    # print(out_f)


for ssp in ("ssp1", "ssp2", "ssp3"):
    for rcp in ("2p6", "4p5", "6p0", "8p5"):
        main(ssp, rcp)