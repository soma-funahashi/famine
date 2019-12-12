###########################################################
#to          : compare the model output with the database
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/10/15
###########################################################

import numpy as np
import pandas as pd
import csv

### setting
prj="dflt"                                            # project name (4 letters)

### file
dfo = pd.read_csv("../dat/fam/famineData.csv")            # famine database
dfm = pd.read_csv("../out/" + prj + "____rslt.csv")        # model output
dfd = pd.DataFrame(index= dfo["ISO3"])              # output dataframe

### main function
def main():
    cnt = dfd.index.values.tolist()                   # list of countries
    ctb = []                                          # right predicted countries
    cto = []                                          # over-predicted countries
    ctm = []                                          # under-predicted countries
    ctn = []                                          # neither case
    doa = dfo.max(axis=1)                             # whether famine occurred or not
    dma = dfm.max(axis=1)                             # worst phase of all period
    tmp = []                                          # result
    phs = []                                          # phase

    for i in range(len(dfo)):
        if   doa[i] == 1 and dma[i] == 3:
            ctb.append(cnt[i])
            tmp.append("b")
            phs.append(dma[i])
        elif doa[i] == 1 and dma[i] != 3:
            cto.append(cnt[i])
            tmp.append("o")
            phs.append(dma[i])
        elif doa[i] == 0 and dma[i] == 3:
            ctm.append(cnt[i])
            tmp.append("m")
            phs.append(dma[i])
        else:
            ctn.append(cnt[i])
            tmp.append("n")
            phs.append(dma[i])

    print("both     :", ctb)
    print("only obs :", cto)
    print("only mdl :", ctm)
    print("neither  :", ctn)
    print("both     :", len(ctb))
    print("only obs :", len(cto))
    print("only mdl :", len(ctm))
    print("neither  :", len(ctn))
    dfd["Result"] = tmp
    dfd["Phase"]  = phs
    dfd.to_csv("../out/"+prj+"____vald.csv")

main()
