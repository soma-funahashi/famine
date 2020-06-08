import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve


gdp = pd.read_csv("../dat/gdp/gdp_per_cap_filled.csv")
upp = pd.read_csv("../dat/upp/upp_new_filled.csv")
cor = pd.read_csv("../dat/cor/correlation_data.csv")
fam = pd.read_csv("../dat/fam/famineData_drought.csv")
drt = pd.read_csv("../dat/sow/drought_flag_15.csv")

def main():
    gl = []
    ul = []
    cl = []
    dl = []
    fl = []
    cnt = 0
    for i in range(len(gdp)):
        for yr in range(1961,2019):
#           X.append([gdp.iat[i, yr - 1960], upp.iat[i, yr - 1960], cor.iat[i, 1]])
#           X.append([gdp.iat[i, yr - 1960]])
#           Y.append(fam.iat[i, yr - 1961])
            gl.append(gdp.iat[i, yr - 1959])
            ul.append(upp.iat[i, yr - 1959])
            cl.append(cor.iat[i, 1])
            dl.append(upp.iat[i, yr - 1960])
            fl.append(fam.iat[i, yr - 1960])
            cnt += 1

    X = pd.DataFrame()
    Y = pd.DataFrame()
    X["gdp"] = gl
    X["upp"] = ul
    X["cor"] = cl
    X["drt"] = dl
    Y["fam"] = fl
    vals = "gucd"

    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
    lr = LogisticRegression()
    lr.fit(X_train, Y_train)

    Y_pred = lr.predict(X_test)

    print(X.shape, Y.shape)
    print("coefficient = ", lr.coef_)
    print("intercept = ", lr.intercept_)
    probs = lr.predict_proba(X)
    print(probs.shape)

    tmp = []
    for i in range(len(probs)):
        tmp.append(probs[i][1])
    tmp = np.array(tmp)
    tmp = tmp.reshape([162, 58])

    print("shape =", tmp.shape)

    out = pd.DataFrame(index = gdp["ISO3"])
    for yr in range(1961, 2019):
        tmp2 = []
        for i in range(len(gdp)):
            tmp2.append(tmp[i][yr-1961])

        out[str(yr)] = tmp2
    out.to_csv("../out/logisticRegression_" + vals + ".csv")
    print(out)

main()