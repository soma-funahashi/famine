import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import statsmodels.api as sm
import sklearn
from sklearn.feature_selection import RFE
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import classification_report
from matplotlib.font_manager import FontProperties
from sklearn.metrics import precision_recall_curve


X = pd.DataFrame()
Y = pd.DataFrame()

def prep():
    gdp = pd.read_csv("../dat/fpi/gdp_per_cap_fpi.csv", index_col="ISO3")
    upp = pd.read_csv("../dat/upp/upp_new_filled.csv", index_col="ISO3")
    cor = pd.read_csv("../dat/cor/correlation_data.csv", index_col="ISO3")
    gin = pd.read_csv("../dat/gin/gini_coeff_ave.csv", index_col="ISO3")
    war = pd.read_csv("../dat/war/war_prob.csv", index_col="ISO3")
    sow = pd.read_csv("../dat/sow/soilmois_cropland_kg_merged.csv", index_col="ISO3")
    fam = pd.read_csv("../dat/fam/famineData_around.csv", index_col="ISO3")
    gin = gin.fillna(gin.mean())
    upp = upp.fillna(0)

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

    X["gdp"] = gl
    X["upp"] = ul
    X["cor"] = cl
    X["gin"] = il
    X["war"] = wl
    X["sow"] = sl
    Y["fam"] = fl
    vals = "all"

prep()


logreg = LogisticRegression()
 
rfe = RFE(logreg, 17) #ランキングトップ17の説明変数を選択する
rfe = rfe.fit(X, Y)
 
#RFEの結果から有効な説明変数を絞り込む
col_name = pd.DataFrame(X.columns).rename(columns = {0:'columns'})
target = pd.DataFrame(rfe.support_).rename(columns = {0:'target'})
all_features = pd.concat([col_name, target], axis = 1)
selected_features = all_features[all_features['target'] == True]
 
print(selected_features)

#RFEから選択された変数だけのデータに整理する
selected_X = X[selected_features['columns']]


#各変数について、学習用データとテスト用データに分割する
X_train, X_test, Y_train, Y_test = train_test_split(selected_X, Y, test_size = 0.2, random_state = 0)
 
#scikit-learnでロジスティック回帰モデルを推定する
logreg = LogisticRegression(fit_intercept = False)
logreg.fit(X_train, Y_train)

kfold = model_selection.KFold(n_splits = 5, shuffle = True, random_state = 42)
model_to_CV = LogisticRegression()

scoring = ['precision_macro', 'recall_macro', 'accuracy', 'f1']
results = model_selection.cross_val_score(model_to_CV, selected_X, Y, cv = kfold, scoring = scoring[2])

print("5-fold Cross Validation Average Accuracy: %.2f" % (results.mean()))


Y_pred = (logreg.predict_proba(X_test)[:, 1] > 0.1).astype(int)
print(confusion_matrix(Y_test, Y_pred, labels=[1, 0]))
print(classification_report(Y_test, Y_pred))

#print(sorted(sklearn.metrics.SCORERS.keys()))

# precision, recall, threshold = precision_recall_curve(Y_test, logreg.predict_proba(X_test)[:, 1])

# # 0から1まで0.05刻みで○をプロット
# for i in range(21):
#     close_point = np.argmin(np.abs(threshold - (i * 0.05)))
#     plt.plot(precision[close_point], recall[close_point], 'o')

# # 適合率-再現率曲線
# plt.plot(precision, recall)
# plt.xlabel('Precision')
# plt.ylabel('Recall')

# plt.show()