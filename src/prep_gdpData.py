import pandas as pd
import numpy as np

iso = pd.read_csv("../dat/nat/nationCode.csv")

ssp = "ssp2"

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


def prep_gdp_future_year():
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



def prep_gdp_per_cap_future_year():
    inpf_gdp = pd.read_csv("../dat/gdp/gdp_" + ssp + "_cnt_year.csv")
    inpf_pop = pd.read_csv("../dat/pop/pop_" + ssp + "_cnt_year.csv")
    gdp_p = pd.read_csv("../dat/gdp/gdp_per_cap_filled.csv")

    out = pd.DataFrame(index=iso["ISO3"])
    for yr in range(2020, 2101):
        tmp = []
        for i in range(len(inpf_gdp)):
            tmp1 = gdp_p["2018"][i]
            tmp2 = inpf_gdp["2020"][i] * 1000000000 / inpf_pop["2020"][i]
            ratio = tmp1 / tmp2
            tmp.append(ratio * inpf_gdp[str(yr)][i] * 1000000000 / inpf_pop[str(yr)][i])
        out[str(yr)] = tmp
        print(yr)
        
    out.to_csv("../dat/gdp/gdp_per_cap_" + ssp + ".csv")


def prep_gdp_per_cap_fpi():
    gdp = pd.read_csv("../dat/gdp/gdp_per_cap_filled.csv")
    fpi = pd.read_csv("../dat/fpi/food_price_index_nominal_real_mar.csv", skiprows = 3)
    print(fpi)
    fpi_list = []
    for i in range(len(fpi)):
        fpi_list.append(fpi.iat[i, 1])
    
    out = pd.DataFrame(index=iso["ISO3"])
    for yr in range(1960, 2019):
        tmp = []
        for i in range(len(gdp)):
            ratio = fpi_list[yr - 1960] / 100
            tmp.append(gdp[str(yr)][i] / ratio)
        out[str(yr)] = tmp
        print(yr)
    out.to_csv("../dat/fpi/gdp_per_cap_fpi.csv")




prep_gdp_per_cap_fpi()

#prep_gdp_future()
#prep_gdp_future_year()
#prep_gdp_per_cap_future_year()