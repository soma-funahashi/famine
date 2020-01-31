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

def prep_gdp_future():
    ssp = "ssp1"
    inp = pd.read_csv("../dat/gdp/gdp_" + ssp + ".csv")
    print(inp.columns)
    out = pd.DataFrame(index=iso["ISO3"], columns = np.arange(2020,2110,10))
    for i in range(len(iso)):
        cnt = iso["ISO3"][i]
        tmp = np.zeros(13)
        for k in range(len(inp)):
            if inp["ISO3"][k] == cnt:
                data = inp.values
                data = data[k, 4:]
                tmp  = data + tmp
        for l in range(len(tmp)):
            print(cnt, inp.columns[l+4], tmp[l])
        out.loc[cnt] = tmp[4:]
    out.to_csv("../dat/gdp/gdp_" + ssp + "_cnt.csv")

#prep_gdp_future()


def prep_gdp_future_year():
    ssp = "ssp1"
    inpf = pd.read_csv("../dat/gdp/gdp_" + ssp + "_cnt.csv")
    out = pd.DataFrame(index=iso["ISO3"], columns = np.arange(2020,2101))
    yl = [2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
    for k in range(len(iso)):
        for i in range(len(inpf)):
            if inpf["ISO3"][i] == iso["ISO3"][k]:
                obs = inpf[i:i+1]
                obs = obs.values[0][1:]
                obs = obs.astype(np.float32)
                tmp = [obs[0]]
                for m in range(len(yl)-1):
                    d = obs[m + 1] - obs[m]
                    for j in range(10):
                        tmp.append(obs[m] + (j + 1) * d / 10)
                #tmp.append(obs[-1])
                out.loc[iso["ISO3"][k]] = tmp
    print(out)
    out.to_csv("../dat/gdp/gdp_" + ssp + "_cnt_year.csv")

prep_gdp_future_year()