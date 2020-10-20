import numpy as np
import pandas as pd

def read_data(ssp, rcp):
    out = pd.read_csv("../out/logisticRegression_all_future_"+ssp+"_rcp"+rcp+".csv", index_col="ISO3")
    return out

out_ssp1_rcp2p6 = read_data("ssp1", "2p6")
out_ssp1_rcp4p5 = read_data("ssp1", "4p5")
out_ssp1_rcp6p0 = read_data("ssp1", "6p0")
out_ssp1_rcp8p5 = read_data("ssp1", "8p5")

out_ssp2_rcp2p6 = read_data("ssp2", "2p6")
out_ssp2_rcp4p5 = read_data("ssp2", "4p5")
out_ssp2_rcp6p0 = read_data("ssp2", "6p0")
out_ssp2_rcp8p5 = read_data("ssp2", "8p5")

out_ssp3_rcp2p6 = read_data("ssp3", "2p6")
out_ssp3_rcp4p5 = read_data("ssp3", "4p5")
out_ssp3_rcp6p0 = read_data("ssp3", "6p0")
out_ssp3_rcp8p5 = read_data("ssp3", "8p5")

ssp1 = out_ssp1_rcp2p6
ssp1 += out_ssp1_rcp4p5
ssp1 += out_ssp1_rcp6p0
ssp1 += out_ssp1_rcp8p5
ssp1 /= 4

ssp2 = out_ssp2_rcp2p6
ssp2 += out_ssp2_rcp4p5
ssp2 += out_ssp2_rcp6p0
ssp2 += out_ssp2_rcp8p5
ssp2 /= 4

ssp3 = out_ssp3_rcp2p6
ssp3 += out_ssp3_rcp4p5
ssp3 += out_ssp3_rcp6p0
ssp3 += out_ssp3_rcp8p5
ssp3 /= 4

print(ssp3)
ssp1.to_csv("../out/logisticRegression_all_future_ssp1_ave.csv")
ssp2.to_csv("../out/logisticRegression_all_future_ssp2_ave.csv")
ssp3.to_csv("../out/logisticRegression_all_future_ssp3_ave.csv")