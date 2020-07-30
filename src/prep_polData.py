import numpy as np
import pandas as pd

org = pd.read_csv("../dat/pol/FAOSTAT_data_7-20-2020.csv")
iso = pd.read_csv("../dat/nat/nationCode.csv")

yl = np.arange(2000, 2019).astype(int)

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

print(out)
out.to_csv("../dat/pol/political_stability.csv")