###########################################################
#to          : convert the database into model input
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/12/25
###########################################################
import pandas as pd
import numpy as np

df0=pd.read_csv("../dat/fam/famineDB_190921.csv")
df1=pd.read_csv("../dat/cor/correlation.csv")
df2=pd.read_csv("../dat/pop/population_inp.csv")

def famineData(df0,df1):
    out=pd.DataFrame(index=df1["ISO3"], columns=np.arange(1961,2020))
    out=out.fillna(0)

    for i in range(len(df0)):
        syr=int(df0.iloc[i,2])
        eyr=int(df0.iloc[i,3])
        cnt=str(df0.iloc[i,5])
        if syr>=1961 and eyr<=2019:
            for k in range(syr,eyr+1):
                out.loc[[cnt],[k]]=1

    out.to_csv("../dat/fam/famineData.csv")


def famineDataNumber(df0,df1):
    out=pd.DataFrame(index=df1["ISO3"], columns=np.arange(1961,2020))
    out=out.fillna(0)

    for i in range(len(df0)):
        syr=int(df0.iloc[i,2])
        eyr=int(df0.iloc[i,3])
        cnt=str(df0.iloc[i,5])
        cas=int(df0.iloc[i,6])
        if syr>=1961 and eyr<=2019:
            for k in range(syr,eyr+1):
                out.loc[[cnt],[k]]=cas

    out.to_csv("../dat/fam/famineDataNumber.csv")

def famineDataNumberRate(df0,df1,df2):
    out=pd.DataFrame(index=df1["ISO3"], columns=np.arange(1961,2020))
    out=out.fillna(0)

    for i in range(len(df0)):
        syr=int(df0.iloc[i,2])
        eyr=int(df0.iloc[i,3])
        cnt=str(df0.iloc[i,5])
        cas=int(df0.iloc[i,6])
        if syr>=1961 and eyr<=2019:
            for k in range(syr,eyr+1):
                pop=int(df2[str(k)][i])
                out.loc[[cnt],[k]]=float(cas)/pop

    out.to_csv("../dat/fam/famineDataNumberRate.csv")

famineDataNumberRate(df0,df1,df2)
