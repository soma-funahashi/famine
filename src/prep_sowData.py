import numpy as np
import pandas as pd

iso = pd.read_csv("../dat/nat/nationCode.csv")

inp_rcp2p6 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp2p6.csv", index_col = "ISO3")
inp_rcp4p5 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp4p5.csv", index_col = "ISO3")
inp_rcp6p0 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp6p0.csv", index_col = "ISO3")
inp_rcp8p5 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp8p5.csv", index_col = "ISO3")

out = pd.read_csv("../dat/sow/soilmois_cropland_ave_hist.csv", index_col = "ISO3")
out = out.drop("2005", axis = 1)

for y in range(2005, 2020):
    print(y)
    for i in range(len(iso)):
        dat = 0
        dat += inp_rcp2p6.at[iso["ISO3"][i], str(y)]
        dat += inp_rcp4p5.at[iso["ISO3"][i], str(y)]
        dat += inp_rcp6p0.at[iso["ISO3"][i], str(y)]
        dat += inp_rcp8p5.at[iso["ISO3"][i], str(y)]
        out.at[iso["ISO3"][i], str(y)] = dat / 4
    out.to_csv("../dat/sow/soilmois_cropland_ave_1971_2019.csv")

print(out)