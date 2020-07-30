import pandas as pd
import numpy as np


def calc_cor():
    df0 = pd.read_csv("../dat/vap/vap_inp_archived.csv")            #1961-2016
    df1 = pd.read_csv("../dat/aws/mod2_SupAgr__WFDELECD.csv")       #1979-2014
    df0 = df0.fillna(0)
    out = pd.DataFrame(index=df0["ISO3"])
    tmp = []
    syr = 1979
    eyr = 2016
    tiny = 1e-15

    for i in range(len(out)):
        a1 = df0.values[i][syr-1961+1:eyr-1961]
        a2 = df1.values[i][1:]
        a1 = a1.astype(float)
        a2 = a2.astype(float)
        a1[0] += tiny
        a2[0] += tiny
        res = np.corrcoef([a1,a2])
        tmp.append(res[0][1])
        print(df0["ISO3"][i],res[0][1])
    out["cor"] = tmp
    # out.to_csv("../dat/cor/correlation_data.csv")
calc_cor()

def check_cor():
    mo = pd.read_csv("../dat/cor/correlation.csv")
    sf = pd.read_csv("../dat/cor/correlation_data.csv")
    cnt = 1
    for i in range(len(mo)):
        flag = "DIFF"
        tmp = 0
        if sf["cor"][i] >= 0.15:
            tmp = 1
        if tmp == mo["cor"][i]:
            flag = "SAME"
            cnt += 1
        print(flag, "okaneya :", mo["cor"][i],"funahashi :", tmp, np.round(sf["cor"][i],4))
    print(cnt)
#check_cor()
