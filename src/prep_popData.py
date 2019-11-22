###########################################################
#to          : convert the database into model input
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/11/21
###########################################################
import pandas as pd
import numpy as np

df0 = pd.read_csv("../dat/pop/population_org.csv", skiprows=1)
df1 = pd.read_csv("../dat/cor/correlation.csv")

cnl = []

for i in range(len(df0)):
    if df0["Type"][i] == "Country/Area":
        cnl.append(df0["Region, subregion, country or area"][i])

out = pd.DataFrame(index=cnl)

def prep1():
    for yr in range(1950,2020):
        tmp = []
        for k in range(len(cnl)):
            for i in range(len(df0)):
                if df0["Region, subregion, country or area"][i] == cnl[k]:
                    tmp.append(int(df0[str(yr)][i])*1000)
        out[str(yr)] = tmp
        print(yr)
    out.to_csv("../dat/pop/population.csv")

def prep2():
    nat = pd.read_csv("../dat/nat/nat_msk.csv")
    fin = pd.read_csv("../dat/pop/population.csv") 
    out = pd.DataFrame(index = nat["ISO3"], columns=np.arange(1950,2020))
    for i in range(len(nat)):
        tmp = []
        for k in range(len(fin)):
            if nat["Country"][i] == fin["Country"][k]:
                for y in range(1950,2020):
                    out[y][i] = fin[str(y)][k]
    out.to_csv("../dat/pop/population_inp.csv")
    print(out)

#prep1()
prep2()
