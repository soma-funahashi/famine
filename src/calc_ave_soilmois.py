import numpy as np
import pandas as pd

def hist():
    gcm1 = pd.read_csv("../dat/sow/soilmois_cropland_gcm1_hist.csv", index_col=0)
    gcm2 = pd.read_csv("../dat/sow/soilmois_cropland_gcm2_hist.csv", index_col=0)
    gcm3 = pd.read_csv("../dat/sow/soilmois_cropland_gcm3_hist.csv", index_col=0)
    gcm4 = pd.read_csv("../dat/sow/soilmois_cropland_gcm4_hist.csv", index_col=0)
    gcm5 = pd.read_csv("../dat/sow/soilmois_cropland_gcm5_hist.csv", index_col=0)
    ave = gcm1 + gcm2 + gcm3 + gcm4 + gcm5

    ave /= 5
    ave.to_csv("../dat/sow/soilmois_cropland_ave_hist.csv")

def calc_2005():
    gcm2 = pd.read_csv("../dat/sow/soilmois_cropland_gcm2_hist.csv", index_col=0)
    gcm3 = pd.read_csv("../dat/sow/soilmois_cropland_gcm3_hist.csv", index_col=0)
    gcm4 = pd.read_csv("../dat/sow/soilmois_cropland_gcm4_hist.csv", index_col=0)
    gcm5 = pd.read_csv("../dat/sow/soilmois_cropland_gcm5_hist.csv", index_col=0)
    
    gcm2_2005 = gcm2["2005"]
    gcm3_2005 = gcm3["2005"]
    gcm4_2005 = gcm4["2005"]
    gcm5_2005 = gcm5["2005"]

    for rcp in (["rcp2p6", "rcp4p5", "rcp6p0", "rcp8p5"]):
        gcm1 = pd.read_csv("../dat/sow/soilmois_cropland_gcm1_"+rcp+".csv", index_col=0)
        gcm1_2005 = gcm1["2005"]
        
        ave = gcm1_2005 + gcm2_2005 + gcm3_2005 + gcm4_2005 + gcm5_2005
        ave /= 5
        print(ave)

        ave.to_csv("../dat/sow/soilmois_cropland_2005_ave_"+rcp+".csv", header = None)


def future():
    for rcp in (["rcp2p6", "rcp4p5", "rcp6p0", "rcp8p5"]):
        gcm1 = pd.read_csv("../dat/sow/soilmois_cropland_gcm1_"+rcp+".csv", index_col=0)
        gcm2 = pd.read_csv("../dat/sow/soilmois_cropland_gcm2_"+rcp+".csv", index_col=0)
        gcm3 = pd.read_csv("../dat/sow/soilmois_cropland_gcm3_"+rcp+".csv", index_col=0)
        gcm4 = pd.read_csv("../dat/sow/soilmois_cropland_gcm4_"+rcp+".csv", index_col=0)
        gcm5 = pd.read_csv("../dat/sow/soilmois_cropland_gcm5_"+rcp+".csv", index_col=0)
        ave = gcm1 + gcm2 + gcm3 + gcm4 + gcm5
        ave /= 5

        dat_2005 = pd.read_csv("../dat/sow/soilmois_cropland_2005_ave_"+rcp+".csv", index_col=0)
        dat_2005 = dat_2005.values

        print(ave)

        ave.to_csv("../dat/sow/soilmois_cropland_ave_"+rcp+".csv")

#future()
