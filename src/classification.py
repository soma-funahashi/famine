import numpy as np
import pandas as pd

gpi = pd.read_csv("../dat/gpi/global_peace_index.csv")
gpi = gpi.mean(axis="columns")
cor = pd.read_csv("../dat/cor/correlation_data.csv")
fam = pd.read_csv("../dat/fam/famineData.csv")
fam = fam.sum(axis="columns")


cnt=0
for i in range(len(gpi)):
    if cor["cor"][i]>=0.2 or gpi[i]>=2.9:
        print(fam[i],cor["ISO3"][i],gpi[i],cor["cor"][i])
        cnt+=1
    else:
        if fam[i]>=1:
            print("hoge")
            print(cor["ISO3"][i])
print(cnt)