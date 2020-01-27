import pandas as pd
import numpy as np
import scipy

iso = pd.read_csv("../dat/nat/nationCode.csv")


def prep_upp_past():
    inp = pd.read_csv("../dat/upp/upp_org.csv",skiprows=4)
    cnt = iso["ISO3"]
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
    out.to_csv("../dat/upp/upp_new.csv")


def prep_upp_future():
    inpf = pd.read_csv("../dat/upp/upp_future_org.csv")
    out = pd.DataFrame(index=iso["ISO3"], columns = np.arange(2020,2051))
    yl = [2020, 2025, 2030, 2035, 2040, 2045, 2050]
    for k in range(len(iso)):
        for i in range(len(inpf)):
            if inpf["Major area, region, country or area"][i] == iso["Country"][k]:
                obs = inpf[i:i+1]
                obs = obs.values[0][1:]
                obs = obs.astype(np.float32)
                coeff = np.polyfit(yl, obs, 1)
                a = coeff[0]
                b = coeff[1]
                print(iso["ISO3"][k], a, b)
                tmp = []
                for yr in range(2020,2051):
                    tmp.append(a * yr + b)
                out.loc[iso["ISO3"][k]] = tmp
    print(out)
    out.to_csv("../dat/upp/upp_future.csv")
prep_upp_future()