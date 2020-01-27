import pandas as pd
import numpy as np

iso = pd.read_csv("../dat/nat/nationCode.csv")


def prep_gdp_past():
    inp = pd.read_csv("../dat/gdp/gdp_per_cap_org.csv",skiprows=4)
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

    out.to_csv("../dat/gdp/gdp_per_cap_new.csv")


