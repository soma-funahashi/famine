import pandas as pd
import numpy as np

iso = pd.read_csv("../dat/nat/nationCode.csv")
inp = pd.read_csv("../dat/gpi/gpi_org2.csv")

cnt = iso["ISO3"]

out = pd.DataFrame(index=iso["ISO3"])

for yr in range(2008,2020):
    tmp=[]
    for i in range(len(iso)):
        flag = True
        for k in range(len(inp)):
            if inp["Country"][k]==iso["Country"][i]:
                tmp.append(round(inp[str(yr)][k],3))
                flag=False
            else:
                pass
        if flag:
            print(iso["ISO3"][i])
            tmp.append("")
    print(yr)
    out[str(yr)] = tmp

#out = out.fillna(0)

#for i in range(len(df0)):
#    syr=int(df0.iloc[i,2])
#    eyr=int(df0.iloc[i,3])
#    cnt=str(df0.iloc[i,5])
#    if syr>=1961 and eyr<=2011:
#        for k in range(syr,eyr+1):
#            out.loc[[cnt],[k]]=1
#
out.to_csv("../dat/gpi/global_peace_index.csv")