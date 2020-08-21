import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def filename(fn):
    if fn == "aws":
        fin = "aws/mod2_SupAgr__WFDELECD.csv"
        lab = "Agricultural water input"
    elif fn == "gdp":
        #fin = "fpi/gdp_per_cap_fpi.csv"
        fin = "gdp/gdp_per_cap_log_st.csv"
        lab = "GDP per capita (st)"
    elif fn == "gdpf":
        fin = "gdp/gdp_per_cap_ssp1_st.csv"
        lab = "GDP in the future (SSP1, st)"
    elif fn == "popf":
        fin = "pop/pop_ssp1_cnt_year.csv"
        lab = "Population in the future (SSP1)"
    elif fn == "gpi":
        fin = "gpi/global_peace_index.csv"
        lab = "Global Peace Index"
    elif fn == "upp":
        fin = "upp/upp_st.csv"
        lab = "Urban population rate (st)"
    elif fn == "unr":
        fin = "unr/undernourishment.csv"
        lab = "Undernourished population rate"
    elif fn == "vap":
        fin = "vap/vap_inp.csv"
        lab = "Value of Agricultural Production"
    elif fn == "awspc":
        fin = "aws/aws_per_capita.csv"
        lab = "AWS per capita"
    elif fn == "vappc":
        fin = "vap/vap_per_capita.csv"
        lab = "Value of Agricultural Production per capita (Int.100$/year)"
    elif fn == "out":
        fin = "../out/multipleRegression.csv"
        lab = "Estimated death rate by famine (% of the population)"
    elif fn == "out2":
        fin = "../out/multipleRegression_drought_gdp.csv"
        lab = "Estimated death rate by famine (% of the population)"
    elif fn == "out3":
        fin = "../out/multipleRegression_drought_gdp_cor.csv"
        lab = "Estimated death rate by famine (% of the population)"
    elif fn == "out4":
        fin = "../out/multipleRegression_drought_gdp_upp_cor.csv"
        lab = "Estimated death rate by famine (% of the population)"
    elif fn == "uppf":
        fin = "../dat/upp/upp_future.csv"
        lab = "Urban population rate (Future)"
    elif fn == "imp":
        fin = "../dat/gdp/import_inp_filled.csv"
        lab = "Imported Value / GDP (%)"
    elif fn == "imppc":
        fin = "../dat/gdp/imported_value_per_cap.csv"
        lab = "Imported Value per capita (current USD)"
    elif fn == "fpi":
        fin = "../dat/fpi/gdp_per_cap_fpi.csv"
        lab = "GDP per cap / Food Price index"
    elif fn == "lor":
        fin = "../out/logisticRegression_all.csv"
        lab = "Logistic Regression"
    elif fn == "lorf":
        fin = "../out/logisticRegression_all_future_ssp1_rcp2p6.csv"
        lab = "Logistic Regression (ssp1, rcp2.6)"
    elif fn == "sow":
        fin = "../dat/sow/soilmois_cropland_kg_merged_st.csv"
        lab = "Soil Moisture in cropland (1961 - 2014)"
    elif fn == "sowf":
        fin = "../dat/sow/soilmois_cropland_ave_rcp8p5.csv"
        lab = "Soil Moisture in cropland (RCP8.5, 2005 - 2099)"
    elif fn == "gin":
        fin = "../dat/gin/gini_coeff.csv"
        lab = "Gini Coefficient"
    elif fn == "war":
        fin = "../dat/war/war.csv"
        lab = "War"
    elif fn == "vul":
        fin = "../out/vulnerability.csv"
        lab = "Vulnerability"
    elif fn == "haz":
        fin = "../out/hazard.csv"
        lab = "Hazard"
    elif fn == "rsk":
        fin = "../out/risk.csv"
        lab = "Risk"
    elif fn == "fpr":
        fin = "../dat/fpr/cereal_import_dependency.csv"
        lab = "Cereal import dependency (%, 2001-2016)"
    elif fn == "csp":
        fin = "../dat/csp/domestic_production_consumed.csv"
        lab = "Domestic production consumed per capita (100$, 1961-2016)"
    elif fn == "pol":
        fin = "../dat/pol/political_stability.csv"
        lab = "Political instability (2000-2018)"
    elif fn == "pdi":
        fin = "../dat/pdi/mod3_pdsi.csv"
        lab = "Palmer's Drought Severity Index (1961 - 2018)"

    return [fin, lab]


### edit here   #select from aws, gdp, gpi, unr, upp
dataname = "lor"
logscale = False
saveflag = False
famcheck = True  ### set True for the past dataset

### input data
fn = filename(dataname)
df = pd.read_csv("../../dat/"+fn[0])
syr = int(df.columns[1])
dfp = df.values
dff = pd.read_csv("../../dat/fam/famineDataNumberRate.csv")
dff = dff.set_index("ISO3")
dfg = pd.read_csv("../../dat/gpi/global_peace_index_filled.csv")
fam = pd.read_csv("../../dat/fam/famineData_drought.csv")
fam = fam.sum(axis=1)
gpi = pd.read_csv("../../dat/gpi/global_peace_index_filled.csv")
gpi = gpi.mean(axis="columns")
cor = pd.read_csv("../../dat/cor/correlation_data.csv")
cor = cor.mean(axis="columns")

yl = df.columns[1:]
yl = yl.astype("int")
yl = np.array(yl)
print(yl)

### model output
prj = "dflt"
#df3 = pd.read_csv("../../out/"+prj+"____vald.csv")
#val = df3["Result"]

plt.figure(figsize=(8,6))

for i in range(1,len(dfp)):
    tmp = dfp[i][1:]
    tmp = tmp.astype("float32")
    cnt = df["ISO3"][i]
    dfs = dff.sum(axis=1)
    if dfs[cnt] > 0:
        plt.plot(yl, tmp, linewidth=0.5, color="red",zorder=50)
#       print(dff.index[i])
#   elif gpi[i]>2.9 or cor[i]>0.2:
#       plt.plot(yl, tmp*100, linewidth=0.5, color="lightgray")
    else:
        plt.plot(yl, tmp, linewidth=0.5, color="lightgray")

if famcheck:
    for y in range(1961,2015):
        for i in range(len(dff)):
            cnt = df["ISO3"][i]
            if dff.loc[cnt, str(y)] != 0:
                print(y, cnt)
                #plt.scatter(y, dfp[i][y - syr + 1], color="Red", s=dff.loc[cnt,str(y)] * 5000, alpha=0.5, linewidths=None, zorder=100)
                plt.scatter(y, dfp[i][y - syr + 1], color="Red", s=10, alpha=0.5, linewidths=None, zorder=100)

# plt.scatter(1965, 300, color="Red", s=0.01*5000, alpha=0.5, linewidths=None, zorder=100)
# plt.scatter(1965, 275, color="Red", s=0.05*5000, alpha=0.5, linewidths=None, zorder=100)
# plt.scatter(1965, 240, color="Red", s=0.1*5000, alpha=0.5, linewidths=None, zorder=100)

if logscale:
    plt.yscale("log")

plt.title(fn[1])

if saveflag:
    if dataname=="awspc":
        plt.savefig("../../fig/aws/"+prj+"____"+dataname+".png",dpi=300,bbox_inches="tight")
    elif dataname=="vappc":
        plt.savefig("../../fig/vap/"+prj+"____"+dataname+".png",dpi=300,bbox_inches="tight")
    elif dataname=="imppc":
        plt.savefig("../../fig/imp/"+prj+"____"+dataname+".png",dpi=300,bbox_inches="tight")
    else:
        plt.savefig("../../fig/"+dataname+"/"+prj+"____"+dataname+".png",dpi=300,bbox_inches="tight")


#plt.savefig("../../fig/multipleRegression_new" + dataname + ".png",dpi=300,bbox_inches="tight")
plt.show()
plt.close()