###########################################################
#to          : calculate per capita data
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/11/25
###########################################################
import pandas as pd
import numpy as np

def calc_perCapita():
#   dfaws = pd.read_csv("../dat/aws/mod2_SupAgr__WFDELECD.csv")       #1979-2014
    dfaws = pd.read_csv("../dat/vap/vap_inp.csv")                     #1961-2016
    dfpop = pd.read_csv("../dat/pop/population_inp.csv")              #1950-2019
    out = pd.DataFrame(index=dfpop["ISO3"])
    
    syr = 1961
    eyr = 2016

    tmp = []
    for i in range(len(out)):
        aws = dfaws.values[i][1:]
        pop = dfpop.values[i][syr-1950+1:eyr-1950+2]
        aws = aws.astype(float)
        pop = pop.astype(float)
        tmp.append(aws/pop)
    
    for y in range(eyr-syr+1):
        o = []
        for i in range(len(out)):
            o.append(tmp[i][y])
        out[str(y+1961)] = o
#   out.to_csv("../dat/aws/aws_per_capita.csv")
    out.to_csv("../dat/vap/vap_per_capita.csv")

calc_perCapita()
