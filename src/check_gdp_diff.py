import numpy as np
import pandas as pd

gdp_p = pd.read_csv("../dat/gdp/gdp_per_cap_filled.csv")
gdp_f = pd.read_csv("../dat/gdp/gdp_ssp1_cnt_year.csv")
gdp_m = pd.read_csv("../dat/gdp/gdp_per_cap_ssp1.csv")
pop_f = pd.read_csv("../dat/pop/pop_ssp1_cnt_year.csv")

for i in range(len(gdp_p)):
    tmp1 = gdp_p["2018"][i]
    tmp2 = gdp_f["2020"][i] * 1000000000 / pop_f["2020"][i]
    tmp3 = gdp_m["2020"][i]
    print(gdp_p["ISO3"][i], tmp1, tmp3)
