import numpy as np
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

gdp = pd.read_csv("../dat/fpi/gdp_per_cap_fpi_st.csv", index_col="ISO3")
upp = pd.read_csv("../dat/upp/upp_new_filled_st.csv", index_col="ISO3")
cor = pd.read_csv("../dat/cor/correlation_data.csv", index_col="ISO3")
gin = pd.read_csv("../dat/gin/gini_coeff_ave.csv", index_col="ISO3")
fam = pd.read_csv("../dat/fam/famineData_all.csv", index_col="ISO3")
war = pd.read_csv("../dat/war/war_wma.csv", index_col="ISO3")
sow = pd.read_csv("../dat/sow/soilmois_cropland_kg.csv", index_col="ISO3")

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
        cl.append(cor.iat[i, 0])
        il.append(gin.iat[i, 0])
        wl.append(war.iat[i, yr - 1960])
        sl.append(sow.iat[i, yr - 1961])
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

print(X.isnull().any())

md = 15

clf = tree.DecisionTreeClassifier(max_depth=md)
clf = clf.fit(X, Y)

predicted = clf.predict(X)

print(predicted)

d = 2015 - 1961

tp = 0
tn = 0
fp = 0
fn = 0

cn = ["Famine", "Not Famine"]
for i in range(len(gdp)):
    for yr in range(d):
        if predicted[d*i+yr] == cn[0] and Y["fam"][d*i+yr] == cn[0]:
            tp += 1
        elif predicted[d*i+yr] == cn[0] and Y["fam"][d*i+yr] == cn[1]:
            fp += 1
        elif predicted[d*i+yr] == cn[1] and Y["fam"][d*i+yr] == cn[0]:
            fn += 1
        elif predicted[d*i+yr] == cn[1] and Y["fam"][d*i+yr] == cn[1]:
            tn += 1

print("True Positive  :", tp)
print("True Negative  :", tn)
print("False Positive :", fp)
print("False Negative :", fn)


fig = plt.figure(figsize = (16,12))
ax = fig.add_subplot()
plot_tree(clf, feature_names=X.columns, ax=ax, class_names=cn, filled=True)
#plt.savefig("../fig/out/decisiontree_" + str(md).zfill(2) + ".png", bbox_inches = "tight", dpi = 300)
plt.show()