import numpy as np
import pandas as pd
import csv

df_obs=pd.read_csv("../dat/famineData.csv")
df_sim=pd.read_csv("../out/famineCountry.csv")

df_dif=pd.DataFrame(index=df_obs["ISO3"])

cnt=df_dif.index.values.tolist()

cnt_os_11=[]
cnt_os_10=[]
cnt_os_01=[]
cnt_os_00=[]

df_obs_all=df_obs.sum(axis=1)
df_sim_all=df_sim.sum(axis=1)

tmp=[]

for i in range(len(df_obs)):
    if df_obs_all[i]>=1 and df_sim_all[i]>=1:
        cnt_os_11.append(cnt[i])
        tmp.append(3)
    elif df_obs_all[i]>=1 and df_sim_all[i]==0:
        cnt_os_10.append(cnt[i])
        tmp.append(2)
    elif df_obs_all[i]==0 and df_sim_all[i]>=1:
        cnt_os_01.append(cnt[i])
        tmp.append(1)
    else:
        cnt_os_00.append(cnt[i])
        tmp.append(0)
print("both     :", cnt_os_11)
print("only obs :", cnt_os_10)
print("only sim :", cnt_os_01)
print("neither  :", cnt_os_00)
df_dif["Result"]=tmp

df_dif.to_csv("../out/validationResult_allperiod.csv")
