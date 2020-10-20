import numpy as np
import pandas as pd

### PREPARATION
def prep():
    years = []
    for y in range(1996, 2019):
        if y != 1997 and y != 1999 and y != 2001:
            years.append(y)
    return years

def main():
    years = prep()
    inp = pd.read_csv("../dat/wgi/wgi_org.csv")
    iso = pd.read_csv("../dat/nat/nationCode.csv", index_col = "ISO3")
    seriesCode = ["CC.EST", "GE.EST", "PV.EST", "RQ.EST", "RL.EST", "VA.EST"]
    for sc in seriesCode:
        out = pd.DataFrame(index = iso.index, columns=np.arange(1996,2019).astype(str))
        for i in range(len(inp)):
            cnt = inp["Country Code"][i]
            if cnt not in iso.index:
                continue
            if inp["Series Code"][i] != sc:
                continue
            print(cnt, sc)
            for y in years:
                out.at[cnt, str(y)] = inp[str(y)][i]
        print(out)
        out.to_csv("../dat/wgi/wgi_"+sc+".csv")
        tmp = pd.read_csv("../dat/wgi/wgi_"+sc+".csv")
        tmp.fillna(tmp.mean(axis = "columns"))
        print(tmp.mean(axis=1))
        tmp.fillna(tmp.mean())
        tmp.to_csv("../dat/wgi/wgi_"+sc+"_st.csv")

if __name__ == "__main__":
    main()