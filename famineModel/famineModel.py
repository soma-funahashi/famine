import numpy as np
import pandas as pd
import csv

df1=pd.read_csv("../famineDB/correlation.csv")
df2=pd.read_csv("../famineDB/gdp_per_cap.csv")
df3=pd.read_csv("../famineDB/urban_population.csv")

yl=np.arange(1961,2012)
cnt=df1["Country"]
out=pd.DataFrame(index=df1["ISO3"])

with open("../out/famineCountryName.csv", "w") as f:
    writer=csv.writer(f)

    for k in range(len(yl)):
        tmp=[]
        tmp2=[]
        year=yl[k]
        l=np.array(df2[str(year)])
        ave_list=np.average(l)
        ave_list=df2.mean()

        for i in range(len(df1)):
            if df1["Correl"][i]==1:
                if df2[str(year)][i]<ave_list[year-1961]:
                    if df3[str(year)][i]<=30:                
                        tmp.append(1)
                        tmp2.append(cnt[i])
                    else:
                        tmp.append(0)
                else:
                    tmp.append(0)
            else:
                tmp.append(0)
        print(year, sum(tmp), tmp2)
        w=[year]+[sum(tmp)]+tmp2
        writer.writerow(w)

        out[str(year)]=tmp

    out.to_csv('../out/famineCountry.csv')
