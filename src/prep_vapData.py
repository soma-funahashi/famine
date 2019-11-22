###########################################################
#to          : convert the vap data into model input
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/11/21
###########################################################

import numpy as np
import pandas as pd
import datetime

df0 = pd.read_csv("../dat/vap/Value_of_Production_E_All_Data_NOFLAG.csv", encoding="ISO-8859-1")
df1 = pd.read_csv("../dat/gdp/gdp_per_cap.csv")
df0 = df0.fillna(0)


def prep_cnl():
    cnl = []
    for k in range(len(df0)-1):
        if df0["Area"][k] == "World":
            break
        elif df0["Area"][k] != df0["Area"][k+1]:
            cnl.append(df0["Area"][k])
    return cnl


def main(cnl):
    l = []
    out = pd.DataFrame(index=cnl, columns=np.arange(1961,2017))
    for k in range(len(cnl)):
        a = np.zeros(56)
        for i in range(len(df0)):
            if df0["Area"][i] == cnl[k]:
                if df0["Element Code"][i] == 152:
                    a = a + df0.values[i][7:63]
        for y in range(1961,2017):
            out[y][k] = a[y-1961]
        print(datetime.datetime.now(), ": completed :", cnl[k])
    out.to_csv("../dat/vap/vap_org.csv")
#cnl = prep_cnl()
#main(cnl)

def prep2():
    nat = pd.read_csv("../dat/nat/nat_msk.csv")
    fin = pd.read_csv("../dat/vap/vap_org.csv")
    out = pd.DataFrame(index = nat["ISO3"], columns=np.arange(1961,2017))
    for i in range(len(nat)):
        tmp = []
        for k in range(len(fin)):
            if nat["Country"][i] == fin["Country"][k]:
                for y in range(1961,2017):
                    out[y][i] = fin[str(y)][k]
    out.to_csv("../dat/vap/vap_inp.csv")
    print(out)

prep2()
