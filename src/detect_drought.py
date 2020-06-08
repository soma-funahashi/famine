import numpy as np
import pandas as pd

df = pd.read_csv("../dat/sow/mod3_soilmois.csv")

per_list = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

for j in range(len(per_list)):
    per = per_list[j]
    thr = df.quantile(per/100, axis=1)
    out = pd.DataFrame(index = df["ISO3"])
    for yr in range(1961, 2020):
        tmp = []
        for i in range(len(df)):
            if df[str(yr)][i] < thr[i]:
                tmp.append(1)
            else:
                tmp.append(0)
        out[str(yr)] = tmp
    out.to_csv('../dat/sow/drought_flag_cropland_' + str(per).zfill(2) + '.csv')
