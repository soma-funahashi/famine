import numpy as np
import pandas as pd
import csv

### setting
prj="dflt"                                            # project name (4 letters)
yrs=np.arange(1961,2019)                              # year

### input file
iso = pd.read_csv("../dat/nat/nationCode.csv")
df1 = pd.read_csv("../dat/cor/correlation_data.csv")       # data of correlation b/w AWI and AP
df2 = pd.read_csv("../dat/gdp/gdp_per_cap.csv")            # data of GDP per capita
df3 = pd.read_csv("../dat/upp/upp_new.csv")                # data of urban population rate

### main function
def main():
    cnt=iso["ISO3"]
    out=pd.DataFrame(index=df1["ISO3"])

    with open("../out/"+prj+"____name.csv", "w") as f:
        writer=csv.writer(f)

        for k in range(len(yrs)):
            tmp1 = []
            tmp2 = []
            yr   = yrs[k]
            avl  = df2.mean()

            for i in range(len(df1)):
                if df1["cor"][i] >= 0.15:
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

#main()


def validation():
    rsl = pd.read_csv('../out/'+prj+'____rslt.csv')
    fam = pd.read_csv('../dat/fam/famineDataNumberRate.csv')
    for i in range(len(rsl)):
        for y in range(1961, 2018):
            if rsl.iloc[i][y-1960] != 3 and float(fam.iloc[i][y-1960]) > 0.0:
                print(y, rsl["ISO3"][i], rsl.iloc[i][y-1960], round(df1["cor"][i],2), round(df2.iloc[i][y-1960],2), round(df3.iloc[i][y-1960],2))

validation()