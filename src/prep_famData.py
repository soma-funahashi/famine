import pandas as pd
import numpy as np

fam = pd.read_csv("../dat/fam/famineDB_190921.csv")
iso = pd.read_csv("../dat/nat/nationCode.csv")
pop = pd.read_csv("../dat/pop/population_inp.csv")

nam = "famineData"
suf = "_all"

def famineData():
    out=pd.DataFrame(index=iso["ISO3"], columns=np.arange(1960,2020))
    out=out.fillna(0)

    for i in range(len(fam)):
        syr = int(fam.iloc[i,2])
        eyr = int(fam.iloc[i,3])
        cnt = str(fam.iloc[i,5])
        flg = str(fam.iloc[i,8])
        if syr>=1961 and eyr<=2019:
#       if syr>=1960 and eyr<=2019 and flg == "1.0":
            for k in range(syr,eyr+1):
                out.loc[[cnt],[k]]=1

    out.to_csv("../dat/fam/" + nam + suf + ".csv")

#famineData()

def famineDataNumber():
    out=pd.DataFrame(index=iso["ISO3"], columns=np.arange(1960,2020))
    out=out.fillna(0)
 
    for i in range(len(fam)):
        syr = int(fam.iloc[i,2])
        eyr = int(fam.iloc[i,3])
        flg = str(fam.iloc[i,8])
        cnt = str(fam.iloc[i,5])
        cas = int(fam.iloc[i,6])/(eyr-syr+1)
        if syr>=1961 and eyr<=2019:
#       if syr>=1960 and eyr<=2019 and flg == "1.0":
            for k in range(syr,eyr+1):
                out.loc[[cnt],[k]]=int(cas)
    out.to_csv("../dat/fam/" + nam + "Number" + suf + ".csv")

#famineDataNumber()



def famineDataNumberRate():
    out=pd.DataFrame(index=iso["ISO3"], columns=np.arange(1960,2020))
#   out=out.fillna(0)
    inp=pd.read_csv("../dat/fam/famineDataNumber" + suf + ".csv")
    for i in range(len(pop)):
        for y in range(1960,2020):
            out[y][i] = float(inp[str(y)][i])/float(pop[str(y)][i])

    out.to_csv("../dat/fam/famineDataNumberRate" + suf + ".csv")

#famineDataNumberRate()


def prep_fam_5yrs(): # average of 5 years
    fam = pd.read_csv("../dat/fam/famineData_all.csv")
    out_sum = pd.DataFrame(index=iso["ISO3"])
    out_max = pd.DataFrame(index=iso["ISO3"])
    for i in range(len(fam)):
        for y in range(1961, 2016, 5):
            print(i, y)
            tmp = fam.loc[i, str(y):str(y+4)]
            out_sum.loc[iso["ISO3"][i], str(y)] = tmp.sum()
            out_max.loc[iso["ISO3"][i], str(y)] = tmp.max()
    out_sum.to_csv("../dat/fam/fam_5yrs_sum.csv")
    out_max.to_csv("../dat/fam/fam_5yrs_max.csv")

#prep_fam_5yrs()

def prep_fam_around():
    fam = pd.read_csv("../dat/fam/famineData_all.csv")
    out = pd.DataFrame(index = iso["ISO3"], columns=np.arange(1961,2015).astype(str))
    r = 3
    for y in range(1961, 2015):
        for i in range(len(iso)):
            if fam[str(y)][i] == 1:
                for k in range(0, r):
                    out[str(max(y-k, 1961))][i] = 1
                    out[str(min(y+k, 2014))][i] = 1
    out = out.fillna(0)
    out.to_csv("../dat/fam/famineData_around.csv")

prep_fam_around()