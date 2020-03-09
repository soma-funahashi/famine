import pandas as pd
import numpy as np

inp = pd.read_csv("../dat/pop/population_org.csv", skiprows=1)
iso = pd.read_csv("../dat/nat/nationCode.csv")

cnl = []

for i in range(len(inp)):
    if inp["Type"][i] == "Country/Area":
        cnl.append(inp["Region, subregion, country or area"][i])
out = pd.DataFrame(index=cnl)

def prep1():
    for yr in range(1950,2020):
        tmp = []
        for k in range(len(cnl)):
            for i in range(len(inp)):
                if inp["Region, subregion, country or area"][i] == cnl[k]:
                    tmp.append(int(inp[str(yr)][i])*1000)
        out[str(yr)] = tmp
        print(yr)
    out.to_csv("../dat/pop/population.csv")
#prep1()

def prep2():
    fin = pd.read_csv("../dat/pop/population.csv")
    out = pd.DataFrame(index = iso["ISO3"], columns=np.arange(1950,2020))
    for i in range(len(iso)):
        for k in range(len(fin)):
            if iso["Country"][i] == fin["Country"][k]:
                for y in range(1950,2020):
                    out[y][i] = fin[str(y)][k]
    out.to_csv("../dat/pop/population_inp.csv")
    print(out)

#prep2()

def prep_pop_future():
    ssp = "ssp3"
    inp = pd.read_csv("../dat/pop/pop_" + ssp + ".csv")
    out = pd.DataFrame(index=iso["ISO3"], columns = np.arange(2020,2110,10))
    for i in range(len(iso)):
        cnt = iso["ISO3"][i]
#        cnt = "JPN"
        tmp = np.zeros(13)
        for k in range(len(inp)):
            if inp["ISO3"][k] == cnt:
                data = inp.values
                data = data[k, 4:]
                tmp  = data * 1000000 + tmp
                tmp = tmp.astype("int")
        for l in range(len(tmp)):
            print(cnt, inp.columns[l+4], tmp[l])
        out.loc[cnt] = tmp[4:]
    
    print(out)
    out.to_csv("../dat/pop/pop_" + ssp + "_cnt.csv")

#prep_pop_future()

def prep_gdp_future_year():
    ssp = "ssp3"
    inpf = pd.read_csv("../dat/pop/pop_" + ssp + "_cnt.csv")
    out = pd.DataFrame(index=iso["ISO3"], columns = np.arange(2020,2101))
    yl = [2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
    for k in range(len(iso)):
        for i in range(len(inpf)):
            if inpf["ISO3"][i] == iso["ISO3"][k]:
                obs = inpf[i:i+1]
                obs = obs.values[0][1:]
                obs = obs.astype(np.float32)   
                tmp = [int(obs[0])]
                for m in range(len(yl)-1):
                    d = obs[m + 1] - obs[m]
                    for j in range(10):
                        tmp.append(int(obs[m] + (j + 1) * d / 10))
                #tmp.append(obs[-1])
                out.loc[iso["ISO3"][k]] = tmp
    print(out)
    out.to_csv("../dat/pop/pop_" + ssp + "_cnt_year.csv")

prep_gdp_future_year()
