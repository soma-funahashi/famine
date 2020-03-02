import pandas as pd
import numpy as np

iso = pd.read_csv("../dat/nat/nationCode.csv")

def prep_imp_past():
    inp = pd.read_csv("../dat/gdp/import_org.csv",skiprows=4)
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

    out.to_csv("../dat/gdp/import_inp.csv")

#prep_imp_past()

def count_mean(inp):
    inp = pd.read_csv("../dat/gdp/import_inp.csv")
    m =inp.mean()
    ans = 0
    for i in range(len(m)):
        ans += m[i]
    return ans / len(m)

def prep_imp_fill():
    inp = np.genfromtxt("../dat/gdp/import_inp.csv", delimiter = ",")
    df  = pd.read_csv("../dat/gdp/import_inp.csv")
    out = pd.DataFrame(index=iso["ISO3"])
    wave = count_mean(inp)
    out1 = []
    for i in range(len(out)):
        tmp  = inp[i + 1][1:]
        if np.isnan(tmp).all():
            ### fill world average
            tmp = [wave] * len(tmp)
        elif np.isnan(tmp).any():
            ### fill country's average
            tmp[np.isnan(tmp)] = np.nanmean(tmp)
            
        print(df["ISO3"][i], tmp)
        
        out1.append(np.array(tmp))

    print(out1)
    print(np.array(out1).shape)

    for j in range(2019 - 1960):
        tmp2 = []
        for i in range(len(out)):
            tmp2.append(out1[i][j])
        out[str(j + 1960)] = tmp2
    print(out)
    out.to_csv("../dat/gdp/import_inp_filled.csv")

prep_imp_fill()

def prep_imp_gdp():
    imp = pd.read_csv("../dat/gdp/import_inp_filled.csv")
    gdp = pd.read_csv("../dat/gdp/gdp_per_cap_filled.csv")
    out = pd.DataFrame(index=iso["ISO3"])
    for y in range(1960, 2019):
        tmp = []
        for i in range(len(out)):
            tmp.append(imp[str(y)][i] * gdp[str(y)][i] / 100)
        out[str(y)] = tmp

    print(out)

    out.to_csv("../dat/gdp/imported_value_per_cap.csv")

prep_imp_gdp()