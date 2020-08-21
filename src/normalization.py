import numpy as np
import scipy.stats
import pandas as pd

eps = 1e-5
iso = pd.read_csv("../dat/nat/nationCode.csv")



def gdpStd():
    gdp = pd.read_csv("../dat/gdp/gdp_per_cap_filled.csv", index_col="ISO3")
    ssp1 = pd.read_csv("../dat/gdp/gdp_per_cap_ssp1.csv", index_col="ISO3")
    ssp2 = pd.read_csv("../dat/gdp/gdp_per_cap_ssp2.csv", index_col="ISO3")
    ssp3 = pd.read_csv("../dat/gdp/gdp_per_cap_ssp3.csv", index_col="ISO3")
    
    des = gdp.T.describe()
    print(des)
    values = gdp.values
    print(values)
    for i in values:
        print(i)
    std = np.std(values)
    mean = np.mean(values)
    print(std)
    print(mean)

    out = pd.DataFrame(index=iso["ISO3"], columns=np.arange(1961,2019).astype(str))
    out_ssp1 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))
    out_ssp2 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))
    out_ssp3 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))

    for i in range(len(gdp)):
        for y in range(1961, 2019):
            out[str(y)][i] = (gdp[str(y)][i] - mean) / (std + eps)
        for y in range(2020, 2100):
            out_ssp1[str(y)][i] = (ssp1[str(y)][i] - mean) / (std + eps)
            out_ssp2[str(y)][i] = (ssp2[str(y)][i] - mean) / (std + eps)
            out_ssp3[str(y)][i] = (ssp3[str(y)][i] - mean) / (std + eps)
    print(out)
    out.to_csv("../dat/gdp/gdp_per_cap_st.csv")
    out_ssp1.to_csv("../dat/gdp/gdp_per_cap_ssp1_st.csv")
    out_ssp2.to_csv("../dat/gdp/gdp_per_cap_ssp2_st.csv")
    out_ssp3.to_csv("../dat/gdp/gdp_per_cap_ssp3_st.csv")

#gdpStd()

def gdpLogStd():
    gdp = pd.read_csv("../dat/gdp/gdp_per_cap_filled.csv", index_col="ISO3")
    ssp1 = pd.read_csv("../dat/gdp/gdp_per_cap_ssp1.csv", index_col="ISO3")
    ssp2 = pd.read_csv("../dat/gdp/gdp_per_cap_ssp2.csv", index_col="ISO3")
    ssp3 = pd.read_csv("../dat/gdp/gdp_per_cap_ssp3.csv", index_col="ISO3")
    gdp = np.log(gdp)
    ssp1 = np.log(ssp1)
    ssp2 = np.log(ssp2)
    ssp3 = np.log(ssp3)

    des = gdp.T.describe()
    print(des)
    values = gdp.values
    print(values)
    std = np.std(values)
    mean = np.mean(values)
    print(std)
    print(mean)

    out = pd.DataFrame(index=iso["ISO3"], columns=np.arange(1961,2019).astype(str))
    out_ssp1 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))
    out_ssp2 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))
    out_ssp3 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))

    for i in range(len(gdp)):
        for y in range(1961, 2019):
            out[str(y)][i] = (gdp[str(y)][i] - mean) / (std + eps)
        for y in range(2020, 2100):
            out_ssp1[str(y)][i] = (ssp1[str(y)][i] - mean) / (std + eps)
            out_ssp2[str(y)][i] = (ssp2[str(y)][i] - mean) / (std + eps)
            out_ssp3[str(y)][i] = (ssp3[str(y)][i] - mean) / (std + eps)
    print(out)
    out.to_csv("../dat/gdp/gdp_per_cap_log_st.csv")
    out_ssp1.to_csv("../dat/gdp/gdp_per_cap_ssp1_log_st.csv")
    out_ssp2.to_csv("../dat/gdp/gdp_per_cap_ssp2_log_st.csv")
    out_ssp3.to_csv("../dat/gdp/gdp_per_cap_ssp3_log_st.csv")

#gdpLogStd()


def uppStd():
    upp = pd.read_csv("../dat/upp/upp_new_filled.csv", index_col="ISO3")
    upp_future = pd.read_csv("../dat/upp/upp_future.csv", index_col="ISO3")

    values = upp.values
    print(values)
    for i in values:
        print(i)
    std = np.std(values)
    mean = np.mean(values)
    print(std)
    print(mean)

    out = pd.DataFrame(index=iso["ISO3"], columns=np.arange(1961,2019).astype(str))
    out_future = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2051).astype(str))

    for i in range(len(upp)):
        for y in range(1961, 2019):
            out[str(y)][i] = (upp[str(y)][i] - mean) / (std + eps)
        for y in range(2020, 2051):
            out_future[str(y)][i] = (upp_future[str(y)][i] - mean) / (std + eps)
    print(out)
    print(out_future)
    out.to_csv("../dat/upp/upp_st.csv")
    out_future.to_csv("../dat/upp/upp_future_st.csv")


#uppStd()


def sowStd1():
    sow = pd.read_csv("../dat/sow/soilmois_cropland_kg_merged.csv", index_col="ISO3")
    sow_2p6 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp2p6.csv", index_col="ISO3")
    sow_4p5 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp4p5.csv", index_col="ISO3")
    sow_6p0 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp6p0.csv", index_col="ISO3")
    sow_8p5 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp8p5.csv", index_col="ISO3")
    
    des = sow.T.describe()
    out = pd.DataFrame(index=iso["ISO3"], columns=np.arange(1961,2015).astype(str)) 
    out_2p6 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))
    out_4p5 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))
    out_6p0 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))
    out_8p5 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))

    for i in range(len(sow)):
        std = des[iso["ISO3"][i]]["std"]
        mean = des[iso["ISO3"][i]]["mean"]
        if iso["ISO3"][i]=="MNE":
            print(iso["ISO3"][i], std, mean)
        for y in range(1961, 2015):
            out[str(y)][i] = (sow[str(y)][i] - mean) / (std + eps)
        for y in range(2020, 2100):
            out_2p6[str(y)][i] = (sow_2p6[str(y)][i] - mean) / (std + eps)
            out_4p5[str(y)][i] = (sow_4p5[str(y)][i] - mean) / (std + eps)
            out_6p0[str(y)][i] = (sow_6p0[str(y)][i] - mean) / (std + eps)
            out_8p5[str(y)][i] = (sow_8p5[str(y)][i] - mean) / (std + eps)
    print(out.T["MNE"])
    out.to_csv("../dat/sow/soilmois_cropland_kg_merged_st.csv")
    out_2p6.to_csv("../dat/sow/soilmois_cropland_ave_rcp2p6_st.csv")
    out_4p5.to_csv("../dat/sow/soilmois_cropland_ave_rcp4p5_st.csv")
    out_6p0.to_csv("../dat/sow/soilmois_cropland_ave_rcp6p0_st.csv")
    out_8p5.to_csv("../dat/sow/soilmois_cropland_ave_rcp8p5_st.csv")

#sowStd1()


def sowStd2():
    sow = pd.read_csv("../dat/sow/soilmois_cropland_kg_merged_na.csv", index_col="ISO3")
    sow_2p6 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp2p6_na.csv", index_col="ISO3")
    sow_4p5 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp4p5_na.csv", index_col="ISO3")
    sow_6p0 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp6p0_na.csv", index_col="ISO3")
    sow_8p5 = pd.read_csv("../dat/sow/soilmois_cropland_ave_rcp8p5_na.csv", index_col="ISO3")
    
    sow = sow.fillna(sow.mean())
    sow_2p6 = sow_2p6.fillna(sow_2p6.mean())
    sow_4p5 = sow_4p5.fillna(sow_4p5.mean())
    sow_6p0 = sow_6p0.fillna(sow_6p0.mean())
    sow_8p5 = sow_8p5.fillna(sow_8p5.mean())

    out = pd.DataFrame(index=iso["ISO3"], columns=np.arange(1961,2015).astype(str)) 
    out_2p6 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))
    out_4p5 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))
    out_6p0 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))
    out_8p5 = pd.DataFrame(index=iso["ISO3"], columns=np.arange(2020,2100).astype(str))

    values = sow.values

    std = np.std(values)
    mean = np.mean(values)
    print(std)
    print(mean)

    for cnt in iso["ISO3"]:
        for y in range(1961, 2015):
            out.at[cnt,str(y)] = (sow.at[cnt,str(y)] - mean) / (std + eps)
        for y in range(2020, 2100):
            out_2p6.at[cnt,str(y)] = (sow_2p6.at[cnt,str(y)] - mean) / (std + eps)
            out_4p5.at[cnt,str(y)] = (sow_4p5.at[cnt,str(y)] - mean) / (std + eps)
            out_6p0.at[cnt,str(y)] = (sow_6p0.at[cnt,str(y)] - mean) / (std + eps)
            out_8p5.at[cnt,str(y)] = (sow_8p5.at[cnt,str(y)] - mean) / (std + eps)
    print(out.T["MNE"])
    out.to_csv("../dat/sow/soilmois_cropland_kg_merged_st.csv")
    out_2p6.to_csv("../dat/sow/soilmois_cropland_ave_rcp2p6_st.csv")
    out_4p5.to_csv("../dat/sow/soilmois_cropland_ave_rcp4p5_st.csv")
    out_6p0.to_csv("../dat/sow/soilmois_cropland_ave_rcp6p0_st.csv")
    out_8p5.to_csv("../dat/sow/soilmois_cropland_ave_rcp8p5_st.csv")

sowStd2()

def singleStd():
    cor = pd.read_csv("../dat/cor/correlation_data.csv", index_col="ISO3")
    gin = pd.read_csv("../dat/gin/gini_coeff_ave.csv", index_col="ISO3")
    war = pd.read_csv("../dat/war/war_prob.csv", index_col="ISO3")
    fpr = pd.read_csv("../dat/fpr/cereal_import_dependency.csv", index_col="ISO3")

    fpr = fpr.mean(axis = 1)

    gin = gin.fillna(gin.mean())

    cor_st = pd.DataFrame(scipy.stats.zscore(cor), index=cor.index, columns=cor.columns)
    gin_st = pd.DataFrame(scipy.stats.zscore(gin), index=gin.index, columns=gin.columns)
    war_st = pd.DataFrame(scipy.stats.zscore(war), index=war.index, columns=war.columns)
    fpr_st = pd.DataFrame(scipy.stats.zscore(fpr), index=war.index, columns=war.columns)

    cor_st.to_csv("../dat/cor/correlation_data_st.csv")
    gin_st.to_csv("../dat/gin/gini_coeff_ave_st.csv")
    war_st.to_csv("../dat/war/war_prob_st.csv")
    fpr_st.to_csv("../dat/fpr/fpr_st.csv")

#singleStd()