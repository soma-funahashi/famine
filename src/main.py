###########################################################
#to          : run the famine detect model
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/10/15
###########################################################

import numpy as np
import pandas as pd
import csv

### setting
prj="dflt"                                            # project name (4 letters)
yrs=np.arange(1961,2012)                              # year

### input file
df1=pd.read_csv("../dat/cor/correlation.csv")             # data of correlation b/w AWI and AP
df2=pd.read_csv("../dat/gdp/gdp_per_cap.csv")             # data of GDP per capita
df3=pd.read_csv("../dat/upp/urban_population.csv")        # data of urban population rate

### main function
def main():
    cnt=df1["Country"]
    out=pd.DataFrame(index=df1["ISO3"])

    with open("../out/"+prj+"____name.csv", "w") as f:
        writer=csv.writer(f)

        for k in range(len(yrs)):
            tmp1 = []
            tmp2 = []
            yr   = yrs[k]
            avl  = df2.mean()

            for i in range(len(df1)):
                if df1["Correl"][i] == 1:
                    if df2[str(yr)][i] < avl[yr-1961]:
                        if df3[str(yr)][i] <= 30:                
                            tmp1.append(3)
                            tmp2.append(cnt[i])
                        else:
                            tmp1.append(2)
                    else:
                        tmp1.append(1)
                else:
                    tmp1.append(0)
            print(yr, np.count_nonzero(np.array(tmp1)==3), tmp2)
            w = [yr] + [np.count_nonzero(np.array(tmp1)==3)] + tmp2
            writer.writerow(w)
            out[str(yr)]=tmp1

        out.to_csv('../out/'+prj+'____rslt.csv')

main()
