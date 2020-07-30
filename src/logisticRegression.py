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

gdp = pd.read_csv("../dat/fpi/gdp_per_cap_fpi.csv", index_col="ISO3")
upp = pd.read_csv("../dat/upp/upp_new_filled.csv", index_col="ISO3")
cor = pd.read_csv("../dat/cor/correlation_data.csv", index_col="ISO3")
gin = pd.read_csv("../dat/gin/gini_coeff_ave.csv", index_col="ISO3")
war = pd.read_csv("../dat/war/war_prob.csv", index_col="ISO3")
sow = pd.read_csv("../dat/sow/soilmois_cropland_kg_merged.csv", index_col="ISO3")

fam = pd.read_csv("../dat/fam/famineData_around.csv", index_col="ISO3")

gin = gin.fillna(gin.mean())
upp = upp.fillna(0)

def main(ssp, rcp):
    gl = []
    ul = []
    cl = []
    il = []
    wl = []
    fl = []
    sl = []
    cnt = 0
    for i in range(len(gdp)):
        for yr in range(1961,2015):
            gl.append(gdp.iat[i, yr - 1960])
            ul.append(upp.iat[i, yr - 1960])
            cl.append(cor.iat[i, 0])
            il.append(gin.iat[i, 0])
            wl.append(war.iat[i, 0])
            fl.append(fam.iat[i, yr - 1961])
            sl.append(sow.iat[i, yr - 1961])
            cnt += 1

    X = pd.DataFrame()
    Y = pd.DataFrame()
    X["gdp"] = gl
    X["upp"] = ul
    X["cor"] = cl
    X["gin"] = il
    X["war"] = wl
    X["sow"] = sl
    Y["fam"] = fl
    vals = "all"
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
    lr = LogisticRegression()
    lr.fit(X_train, Y_train)

    Y_pred = lr.predict(X_test)

    # print(X.shape, Y.shape)
    # print("coefficient = ", lr.coef_)
    # print("intercept = ", lr.intercept_)
    probs = lr.predict_proba(X)
    # print(probs.shape)

    tmp = []
    for i in range(len(probs)):
        tmp.append(probs[i][1])
    tmp = np.array(tmp)
    tmp = tmp.reshape([162, 54])

    # print("shape =", tmp.shape)

    out = pd.DataFrame(index = gdp.index)
    for yr in range(1961, 2015):
        tmp2 = []
        for i in range(len(gdp)):
            tmp2.append(tmp[i][yr-1961])

        out[str(yr)] = tmp2
    out.to_csv("../out/logisticRegression_" + vals + ".csv")
    # print(out)


    X_future = pd.DataFrame()

    gdp_f = pd.read_csv("../dat/gdp/gdp_per_cap_"+ssp+".csv", index_col="ISO3")
    upp_f = pd.read_csv("../dat/upp/upp_future.csv", index_col="ISO3")
    sow_f = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp"+rcp+".csv", index_col="ISO3")

    gdp_f = gdp_f.fillna(gdp_f.mean(axis = 0))

    # for i in range(len(gdp)):
    #     print(gdp_f.iloc[i,:])

    glf = []
    ulf = []
    clf = []
    ilf = []
    wlf = []
    slf = []

    num = 0
    for i in range(len(gdp)):
        for yr in range(2021, 2051):
            glf.append(gdp_f.iat[i, yr - 2021])
            ulf.append(upp_f.iat[i, yr - 2021])
            clf.append(cor.iat[i, 0])
            ilf.append(gin.iat[i, 0])
            wlf.append(war.iat[i, 0])
            slf.append(sow_f.iat[i, yr - 2021])

    X_future["gdp"] = glf
    X_future["upp"] = ulf
    X_future["cor"] = clf
    X_future["gin"] = ilf
    X_future["war"] = wlf
    X_future["sow"] = slf
    # print(X_future.isna().any())

    print(X_future.shape)
    probs_future = lr.predict_proba(X_future)

    # print(probs_future)
    print(probs_future.shape)

    tmp_f = []
    for i in range(162*30):
        tmp_f.append(probs_future[i][1])
    tmp_f = np.array(tmp_f)
    tmp_f = tmp_f.reshape([162, 30])

    print("shape =", tmp_f.shape)

    out_f = pd.DataFrame(index = gdp.index)
    for yr in range(2021, 2051):
        tmp2_f = []
        for i in range(len(gdp)):
            tmp2_f.append(tmp_f[i][yr-2021])

        out_f[str(yr)] = tmp2_f
    out_f.to_csv("../out/logisticRegression_" + vals + "_future_"+ssp+"_rcp"+rcp+".csv")
    print(out_f)


for ssp in ("ssp1", "ssp2", "ssp3"):
    for rcp in ("2p6", "4p5", "6p0", "8p5"):
        main(ssp, rcp)