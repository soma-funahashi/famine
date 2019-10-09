import pandas as pd
import numpy as np

df=pd.read_csv("../famineDB/famineDB_190921.csv")
df1=pd.read_csv("../famineDB/correlation.csv")

out=pd.DataFrame(index=df1["ISO3"],columns=np.arange(1961,2012))
out=out.fillna(0)

for i in range(len(df)):
    syr=int(df.iloc[i,2])
    eyr=int(df.iloc[i,3])
    cnt=str(df.iloc[i,5])
    if syr>=1961 and eyr<=2011:
        for k in range(syr,eyr+1):
            out.loc[[cnt],[k]]=1

out.to_csv("../famineDB/famineData.csv")
