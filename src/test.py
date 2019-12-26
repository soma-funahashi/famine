from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

gdp = pd.read_csv("../dat/gdp/gdp_per_cap_filled.csv")
upp = pd.read_csv("../dat/upp/urban_population_filled.csv")
fam = pd.read_csv("../dat/fam/famineDataNumberRate.csv")

print(len(gdp.columns))
print(len(upp.columns))
print(len(fam.columns))

x = []
y = []

gpi = pd.read_csv("../dat/gpi/global_peace_index.csv")
gpi = gpi.mean(axis="columns")
cor = pd.read_csv("../dat/cor/correlation_data.csv")

gdp2 = gdp.copy()
upp2 = upp.copy()

for i in range(len(gpi)):
    if cor["cor"][i]>=0.2 or gpi[i]>=2.9:
        pass
    else:
        print(cor["cor"][i])
#       gdp2 = gdp2.drop(cor["ISO3"][i])
#       upp2 = upp2.drop(cor["ISO3"][i])

print(gdp2)
print(upp2)

for i in range(len(gdp)):
    for year in range(1961,2012):
        x.append([gdp[str(year)][i],upp[str(year)][i]])
        y.append([fam[str(year)][i]])

x = np.array(x)
y = np.array(y)

print(x)
print(y)

sscaler = preprocessing.StandardScaler()
sscaler.fit(x)
xss_sk = sscaler.transform(x)
sscaler.fit(y)
yss_sk = sscaler.transform(y)

# print(xss_sk)
# print(yss_sk)

mscaler = preprocessing.MinMaxScaler()
mscaler.fit(x)
xms = mscaler.transform(x)
mscaler.fit(y)
yms = mscaler.transform(y)

# print(xms)
# print(yms)



model_lr_std = LinearRegression()
model_lr_std.fit(xss_sk, yss_sk)


print(model_lr_std.coef_)
print(model_lr_std.intercept_)
print(model_lr_std.score(xss_sk, yss_sk))

out = sscaler.inverse_transform(model_lr_std.predict(xss_sk))
out = out.reshape(len(gdp),2012-1961)


out2 = []
for i in range(len(out)):
    out2.append(np.mean(out[i]))
    print(i,out2[i])


out3 = pd.DataFrame(out,index=gdp["ISO3"],columns=gdp.columns[1:])

print(out3)
out3.to_csv("../out/multipleRegression.csv")