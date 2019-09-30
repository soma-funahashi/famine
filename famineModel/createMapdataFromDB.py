import pandas as pd
import numpy as np

df=pd.read_csv("../famineDB/famineDB_190921.csv")
df1=pd.read_csv("../famineDB/correlation.csv")

out=pd.DataFrame(index=df1["ISO3"])
cntout=list(out.index)

for i in range(len(df)):
    cnt=df.ix[[i],["CountryCode"]]
    print(cnt)
    year=np.arange(int(df.iloc[[i],[2]]), int(df.iloc[[i],[3]])+1)
    for k in range(len(out)):
        if cntout[k]==cnt:
            print("yes")
