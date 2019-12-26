###########################################################
#to          : convert the database into model input
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/11/26
###########################################################
import pandas as pd
import numpy as np

df0 = pd.read_csv("../dat/gdp/gdp_per_cap_org.csv",skiprows=4)
df1 = pd.read_csv("../dat/cor/correlation.csv")

cnt = df1["ISO3"]

out = pd.DataFrame(index=df1["ISO3"])

for yr in range(1961,2019):
    tmp=[]
    for i in range(len(df1)):
        flag = True
        for k in range(len(df0)):
            if df0["Country Code"][k]==df1["ISO3"][i]:
                tmp.append(df0[str(yr)][k])
                flag=False
            else:
                pass
        if flag:
            print(df1["ISO3"][i])
            tmp.append("")
    out[str(yr)] = tmp

out.to_csv("../dat/gdp/gdp_per_cap_new.csv")
