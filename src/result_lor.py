import numpy as np
import pandas as pd

fam = pd.read_csv("../dat/fam/famineData_around.csv", index_col="ISO3")
out = pd.read_csv("../out/logisticRegression_all.csv", index_col="ISO3")

#lab = ["0.00~0.05", "0.05~0.10", "0.10~0.20", "0.20~1.00"]
#lab = ["0.00~0.01", "0.01~0.02", "0.02~0.05", "0.05~1.00"]

cnt_t = [0,0,0,0]
cnt_f = [0,0,0,0]

t1 = 0.01
t2 = 0.025
t3 = 0.05

def idx(v):
    if 0 <= v < t1:
        return 0
    elif t1 <= v < t2:
        return 1
    elif t2 <= v < t3:
        return 2
    elif t3 < v:
        return 3

lab = ["0.00~"+str(t1), str(t1)+"~"+str(t2), str(t2)+"~"+str(t3), str(t3)+"~1.00"]

for i in range(len(fam)):
    for y in range(1961,2015):
        val = out[str(y)][i]
        if fam[str(y)][i] == 1:
            cnt_t[idx(val)] += 1
        else:
            cnt_f[idx(val)] += 1

for i in range(4):
    print(lab[i], cnt_t[i], cnt_f[i], cnt_t[i]/(cnt_f[i] + cnt_t[i]))