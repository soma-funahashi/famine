import pandas as pd
import numpy as np

fam=pd.read_csv("../dat/fam/famineDB_190921.csv")
iso=pd.read_csv("../dat/nat/nationCode.csv")
pop=pd.read_csv("../dat/pop/population_inp.csv")

def famineData():
    out=pd.DataFrame(index=iso["ISO3"], columns=np.arange(1961,2020))
    out=out.fillna(0)

    for i in range(len(fam)):
        syr=int(fam.iloc[i,2])
        eyr=int(fam.iloc[i,3])
        cnt=str(fam.iloc[i,5])
        if syr>=1961 and eyr<=2019:
            for k in range(syr,eyr+1):
                out.loc[[cnt],[k]]=1

    out.to_csv("../dat/fam/famineData.csv")

#famineData()

def famineDataNumber():
    out=pd.DataFrame(index=iso["ISO3"], columns=np.arange(1961,2020))
    out=out.fillna(0)

    for i in range(len(fam)):
        syr=int(fam.iloc[i,2])
        eyr=int(fam.iloc[i,3])
        cnt=str(fam.iloc[i,5])
        cas=int(fam.iloc[i,6])/(eyr-syr+1)
        if syr>=1961 and eyr<=2019:
            for k in range(syr,eyr+1):
                out.loc[[cnt],[k]]=int(cas)
    out.to_csv("../dat/fam/famineDataNumber.csv")

famineDataNumber()



def famineDataNumberRate():
    out=pd.DataFrame(index=iso["ISO3"], columns=np.arange(1961,2020))
#   out=out.fillna(0)
    inp=pd.read_csv("../dat/fam/famineDataNumber.csv")
    for i in range(len(pop)):
        for y in range(1961,2020):
            out[y][i] = float(inp[str(y)][i])/float(pop[str(y)][i])

    out.to_csv("../dat/fam/famineDataNumberRate.csv")

famineDataNumberRate()
