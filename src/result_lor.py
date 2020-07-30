import numpy as np
import pandas as pd

fam = pd.read_csv("../dat/fam/famineData_around.csv", index_col="ISO3")
out = pd.read_csv("../out/logisticRegression_all.csv", index_col="ISO3")

lab = ["0.00~0.05", "0.05~0.10", "0.10~0.20", "0.20~1.00"]

cnt_t = [0,0,0,0]
cnt_f = [0,0,0,0]

def idx(v):
    if 0 <= v < 0.05:
        return 0
    elif 0.05 <= v < 0.10:
        return 1
    elif 0.10 <= v < 0.20:
        return 2
    elif 0.20 < v:
        return 3

for i in range(len(fam)):
    for y in range(1961,2015):
        val = out[str(y)][i]
        if fam[str(y)][i] == 1:
            cnt_t[idx(val)] += 1
        else:
            cnt_f[idx(val)] += 1

for i in range(4):
    print(lab[i], cnt_t[i], cnt_f[i])