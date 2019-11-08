###########################################################
#to          : convert the database into model input
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/11/08
###########################################################
import pandas as pd
import numpy as np

df0 = pd.read_csv("../dat/unr/undernourishment.csv", skiprows=4)
df1 = pd.read_csv("../dat/cor/correlation.csv")

cnt = df1["ISO3"]
print(df0["Country Code"])

out = pd.DataFrame(index=df1["ISO3"], columns=np.arange(1961,2012))

for i in range(len(df0)):
    for k in range(len(df1)):
        if df0["Country Code"][i]==df1["ISO3"][k]:
            print(df0.iloc[k,:])


#out = out.fillna(0)

#for i in range(len(df0)):
#    syr=int(df0.iloc[i,2])
#    eyr=int(df0.iloc[i,3])
#    cnt=str(df0.iloc[i,5])
#    if syr>=1961 and eyr<=2011:
#        for k in range(syr,eyr+1):
#            out.loc[[cnt],[k]]=1
#
#out.to_csv("../dat/org/famineData.csv")
