import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

cor = pd.read_csv("../dat/cor/correlation_data.csv")
gdp = pd.read_csv("../dat/gdp/gdp_per_cap.csv")
upp = pd.read_csv("../dat/upp/urban_population.csv")

gdp = gdp.fillna(0)
upp = upp.fillna(upp.mean())

fam = pd.read_csv("../dat/fam/famineDataNumberRate.csv")





# year = 1985

# x1 = cor
# x2 = gdp[str(year)]
# x3 = upp[str(year)]
# x = x1.join(x2)
# x = x.join(x3)
# x = x[["cor",str(year)]]
# #x3 = upp[str(year)]
# y  = fam[[str(year)]]

# sscaler = preprocessing.StandardScaler()
# sscaler.fit(x)
# xss_sk = sscaler.transform(x) 

# sscaler.fit(y)
# yss_sk = sscaler.transform(y)

# print(xss_sk)
# print(yss_sk)

# model_lr_std = LinearRegression()
# model_lr_std.fit(xss_sk, yss_sk)

# print(model_lr_std.coef_)
# print(model_lr_std.intercept_)
# print(model_lr_std.score(xss_sk, yss_sk))

# out = sscaler.inverse_transform(model_lr_std.predict(xss_sk))

# print(out)
# print(out.max())

# x_add_const = sm.add_constant(xss_sk)
# model_sm = sm.OLS(yss_sk, x_add_const).fit()
# print(model_sm.summary())