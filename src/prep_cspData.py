import numpy as np
import pandas as pd

vap = pd.read_csv("../dat/vap/vap_per_capita.csv", index_col="ISO3") ## 1961~2016
fpr = pd.read_csv("../dat/fpr/cereal_import_dependency.csv", index_col="ISO3") ## 2001~2016

fpr = fpr.mean(axis = 1)
fpr.fillna(0)

out = pd.DataFrame(index=vap.index, columns=vap.columns)

eps = 1e-5

for i in range(len(vap)):
    for y in range(1961, 2017):
        if fpr[i] == 100:
            continue
        out[str(y)][i] = vap[str(y)][i] * 100 / (100 - fpr[i] + eps)

out.to_csv("../dat/csp/domestic_production_consumed.csv")