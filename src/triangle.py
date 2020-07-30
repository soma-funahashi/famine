import numpy as np
import pandas as pd

iso = pd.read_csv("../dat/nat/nationCode.csv")

syr = 1961
eyr = 2015
eps = 1e-15

#def calc_exposure(): ### food imported ratio
    



def calc_hazard(): ### soil water & conflict
    war = pd.read_csv("../dat/war/war_wma.csv", index_col="ISO3")
    sow = pd.read_csv("../dat/sow/soilmois_cropland_kg.csv", index_col="ISO3")
    war_norm = (war - war.min()) / (war.max() - war.min() + eps)
    sow_norm = (sow - sow.min()) / (sow.max() - sow.min() + eps)
    war_norm = war_norm.loc[:,str(syr):str(eyr)]
    sow_norm = 1 - sow_norm.loc[:,str(syr):str(eyr)]
    out = war_norm + sow_norm
    out.to_csv("../out/hazard.csv")


def calc_vulnerability(): ### GDP, UPR, COR
    gdp = pd.read_csv("../dat/fpi/gdp_per_cap_fpi.csv", index_col="ISO3") 
    upp = pd.read_csv("../dat/upp/upp_new_filled_st.csv", index_col="ISO3")
    cor = pd.read_csv("../dat/cor/correlation_data_year.csv", index_col="ISO3")
    upp = upp.fillna(upp.mean())
    gdp_norm = (gdp - gdp.values.min()) / (gdp.values.max() - gdp.values.min() + eps)
    upp_norm = (upp - upp.values.min()) / (upp.values.max() - upp.values.min() + eps)
    cor_norm = (cor - cor.values.min()) / (cor.values.max() - cor.values.min() + eps)
    gdp_norm = gdp_norm.loc[:,str(syr):str(eyr)]
    upp_norm = upp_norm.loc[:,str(syr):str(eyr)]
    cor_norm = 1 - cor_norm.loc[:,str(syr):str(eyr)]
    
    out = gdp_norm + upp_norm + cor_norm
    out.to_csv("../out/vulnerability.csv")


def calc_risk():
    haz = pd.read_csv("../out/hazard.csv", index_col="ISO3")
    vul = pd.read_csv("../out/vulnerability.csv", index_col="ISO3")
    out = haz * vul
    out.to_csv("../out/risk.csv")

#calc_hazard()
#calc_vulnerability()
calc_risk()