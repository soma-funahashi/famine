import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

gdp = pd.read_csv("../dat/fpi/gdp_per_cap_fpi_st.csv", index_col="ISO3")
upp = pd.read_csv("../dat/upp/upp_new_filled_st.csv", index_col="ISO3")
cor = pd.read_csv("../dat/cor/correlation_data.csv", index_col="ISO3")
gin = pd.read_csv("../dat/gin/gini_coeff_ave.csv", index_col="ISO3")
sow = pd.read_csv("../dat/sow/soilmois_cropland_kg.csv", index_col="ISO3")
fam = pd.read_csv("../dat/fam/famineData_all.csv", index_col="ISO3")
war = pd.read_csv("../dat/war/war_wma.csv", index_col="ISO3")

gin = gin.fillna(gin.mean())
upp = upp.fillna(0)

gl = []
ul = []
cl = []
il = []
fl = []
wl = []
sl = []

for i in range(len(gdp)):
    for yr in range(1961,2015):
        gl.append(gdp.iat[i, yr - 1960])
        ul.append(upp.iat[i, yr - 1960])
        sl.append(upp.iat[i, yr - 1961])
        cl.append(cor.iat[i, 0])
        il.append(gin.iat[i, 0])
        wl.append(war.iat[i, yr - 1960])
        if fam.iat[i, yr - 1960] == 1:
            fl.append("Famine")
        elif fam.iat[i, yr - 1960] == 0:
            fl.append("Not Famine")

X = pd.DataFrame()
Y = pd.DataFrame()
X["gdp"] = gl
X["upp"] = ul
X["cor"] = cl
#X["gin"] = il
X["war"] = wl
X["sow"] = sl
Y["fam"] = fl

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.9, random_state=0)

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

model = SVC(kernel='linear', random_state=None)

model.fit(X_train_std, y_train)

pred_train = model.predict(X_train_std)
accuracy_train = accuracy_score(y_train, pred_train)
print('トレーニングデータに対する正解率： %.2f' % accuracy_train)

pred_test = model.predict(X_test_std)
accuracy_test = accuracy_score(y_test, pred_test)
print('テストデータに対する正解率： %.2f' % accuracy_test)

mat = confusion_matrix(y_test, pred_test)

print(mat)