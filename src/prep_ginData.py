import pandas as pd
import numpy as np

iso = pd.read_csv("../dat/nat/nationCode.csv")

def prep_gini():
    inp = pd.read_csv("../dat/gin/gini_coeff_org.csv",skiprows=3)
    out = pd.DataFrame(index=iso["ISO3"])

    for yr in range(1960,2019):
        tmp=[]
        for i in range(len(iso)):
            flag = True
            for k in range(len(inp)):
                if inp["Country Code"][k]==iso["ISO3"][i]:
                    tmp.append(inp[str(yr)][k])
                    flag=False
                else:
                    pass
            if flag:
                print(inp["ISO3"][i])
                tmp.append("")
        print(yr)
        out[str(yr)] = tmp

    out.to_csv("../dat/gin/gini_coeff.csv")

#prep_gini()



def gini_ave():
    inp = pd.read_csv("../dat/gin/gini_coeff.csv")
    tmp = inp.mean(axis=1, skipna=True, numeric_only=True)
    print(tmp)
    out = pd.DataFrame(index=iso["ISO3"])
    tmp = np.array(tmp)
    out["average"] = tmp
    out.to_csv("../dat/gin/gini_coeff_ave.csv")

gini_ave()