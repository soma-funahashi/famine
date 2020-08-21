import numpy as np
import pandas as pd

org = pd.read_csv("../dat/fpr/FAOSTAT_data_7-15-2020.csv")
iso = pd.read_csv("../dat/nat/nationCode.csv")
yl = np.arange(20002002, 20162018, 10001)
out = pd.DataFrame(index=iso["ISO3"], columns=yl)


for i in range(len(iso)):
    country = iso["Country"][i]
    nat = iso["ISO3"][i]
    flag = False
    for j in range(len(org)):
        if org["Area"][j] == country:
            out[org["Year Code"][j]][i] = org["Value"][j]
            flag = True
    if not flag:
        print(country)


dic = {}
for y in yl:
    dic[y] = (y%10000 + y//10000)//2

out = out.rename(columns=dic)

out = out.fillna(out.mean())
print(out)
out.to_csv("../dat/fpr/cereal_import_dependency.csv")