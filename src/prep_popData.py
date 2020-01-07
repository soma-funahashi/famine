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

prep2()
