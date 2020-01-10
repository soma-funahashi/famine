from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

gdp = pd.read_csv("../dat/gdp/gdp_per_cap_filled.csv")
upp = pd.read_csv("../dat/upp/urban_population_filled.csv")
cor = pd.read_csv("../dat/cor/correlation_data.csv")
fam = pd.read_csv("../dat/fam/famineDataNumberRate_drought.csv")

gpi = pd.read_csv("../dat/gpi/global_peace_index_filled.csv")
gpi = gpi.mean(axis="columns")
cor = pd.read_csv("../dat/cor/correlation_data.csv")
cor = cor.mean(axis="columns")

def multipleRegression():
    x = []
    y = []
    valueflag = True
    if valueflag:
        for i in range(len(gdp)):
            for year in range(1961,2012):
                x.append([gdp[str(year)][i],upp[str(year)][i],gpi[i],cor[i]])
                y.append([fam[str(year)][i]])
    else:
        for i in range(len(gdp)):
            for year in range(1961,2012):
                x.append([gdp[str(year)][i],upp[str(year)][i]])
                y.append([fam[str(year)][i]])    
        
    x = np.array(x)
    y = np.array(y)

    sscaler = preprocessing.StandardScaler()
    sscaler.fit(x)
    xss_sk = sscaler.transform(x)
    sscaler.fit(y)
    yss_sk = sscaler.transform(y)

    # print(xss_sk)
    # print(yss_sk)

    model_lr_std = LinearRegression()
    model_lr_std.fit(xss_sk, yss_sk)

    print(model_lr_std.coef_)
    print(model_lr_std.intercept_)
    print(model_lr_std.score(xss_sk, yss_sk))

    out = sscaler.inverse_transform(model_lr_std.predict(xss_sk))
    out = out.reshape(len(gdp),2012-1961)

    out3 = pd.DataFrame(out,index=gdp["ISO3"],columns=gdp.columns[1:])

    print(out3)
    if valueflag:
        out3.to_csv("../out/multipleRegression_4values.csv")
    else:
        out3.to_csv("../out/multipleRegression.csv")


def multipleRegression2():
    x = []
    y = []
    cnt = []
    for i in range(len(gdp)):
        if cor[i]>=0.2 or gpi[i]>=2.9:
            cnt.append(gdp["ISO3"][i])
            for year in range(1961,2019):
                x.append([gdp[str(year)][i],upp[str(year)][i]])
                y.append([fam[str(year)][i]])
    print(cnt)
    print(len(cnt))
        
    x = np.array(x)
    y = np.array(y)

    sscaler = preprocessing.StandardScaler()
    sscaler.fit(x)
    xss_sk = sscaler.transform(x)
    sscaler.fit(y)
    yss_sk = sscaler.transform(y)

    model_lr_std = LinearRegression()
    model_lr_std.fit(xss_sk, yss_sk)

    print(model_lr_std.coef_)
    print(model_lr_std.intercept_)
    print(model_lr_std.score(xss_sk, yss_sk))

    out = sscaler.inverse_transform(model_lr_std.predict(xss_sk))
    out = out.reshape(len(cnt),2019-1961)

    out3 = pd.DataFrame(out,index=cnt,columns=gdp.columns[1:])

    print(out3)
    out3.to_csv("../out/multipleRegression_draught.csv")

multipleRegression2()