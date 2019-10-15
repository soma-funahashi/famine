import numpy as np
import pandas as pd
import csv

df_obs=pd.read_csv("../famineDB/famineData.csv")
df_sim=pd.read_csv("../out/famineCountry.csv")

df_dif=pd.DataFrame(index=df_obs["ISO3"])
#print(df_dif)

cnt_os_11=0
cnt_os_10=0
cnt_os_01=0
cnt_os_00=0

for y in range(1961,2012):
    tmp=[]
    for i in range(len(df_obs)):
        if df_obs[str(y)][i]==1 and df_sim[str(y)][i]==1:
            tmp.append(3)
            cnt_os_11+=1
        elif df_obs[str(y)][i]==1 and df_sim[str(y)][i]==0:
            tmp.append(2)
            cnt_os_10+=1
        elif df_obs[str(y)][i]==0 and df_sim[str(y)][i]==1:
            tmp.append(1)
            cnt_os_01+=1
        else:
            tmp.append(0)
            cnt_os_00+=1
    df_dif[str(y)]=tmp
print("both     :", cnt_os_11)
print("only obs :", cnt_os_10)
print("only sim :", cnt_os_01)
print("neither  :", cnt_os_00)
print("accuracy =", (cnt_os_11+cnt_os_00)/(cnt_os_11+cnt_os_10+cnt_os_01+cnt_os_00))
print("threat score  =", cnt_os_11/(cnt_os_11+cnt_os_10+cnt_os_01))
df_dif.to_csv("../out/validationResult.csv")
