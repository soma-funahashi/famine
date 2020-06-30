import numpy as np
import pandas as pd

dat = pd.read_csv("../../dat/fam/tmp.csv")
cat = dat.columns
cat = np.array(cat)
cat = cat[2:]
cat[0] = "year"
print(cat)
dat = dat.fillna(0)
dat = dat.values

array = np.arange(1840, 2020, 10)
out = []

for y in array:
    tmp = [0] * 11
    cnt = 0
    for i in range(len(dat)):
        for j in range(3, 13): ## category
            if y <= dat[i][1] and dat[i][1] < y + 10:
                tmp[j - 3] += dat[i][j]
                cnt += 1
    tmp[10] = cnt // 10
    print(y, tmp)
    out.append(tmp)

out = np.array(out).reshape(len(array), 11)

#out = out.astype("int")
print(out)
out = pd.DataFrame(out)
out.to_csv("../../dat/fam/causes.csv", index = None, columns = None)
#np.savetxt("../../dat/fam/out.csv", out, delimiter = ",",  fmt='%.d')