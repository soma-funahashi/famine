import pandas as pd
import numpy as np

inp = pd.read_csv("../dat/unr/undernourishment_org.csv", skiprows=4)
iso = pd.read_csv("../dat/nat/nationCode.csv")

cnt = iso["ISO3"]
out = pd.DataFrame(index=iso["ISO3"])

for yr in range(2000,2019):
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
            print(iso["ISO3"][i])
            tmp.append("")
    out[str(yr)] = tmp

out.to_csv("../dat/unr/undernourishment.csv")