import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def filename(fn):
    if fn == "aws":
        fin = "aws/mod2_SupAgr__WFDELECD.csv"
        lab = "Agricultural water input"
    elif fn == "gdp":
        fin = "gdp/gdp_per_cap.csv"
        lab = "GDP per capita"
    elif fn == "gdpf":
        fin = "gdp/gdp_ssp1_cnt_year.csv"
        lab = "GDP in the future (SSP1)"
    elif fn == "popf":
        fin = "pop/pop_ssp1_cnt_year.csv"
        lab = "Population in the future (SSP1)"
    elif fn == "gpi":
        fin = "gpi/global_peace_index.csv"
        lab = "Global Peace Index"
    elif fn == "upp":
        fin = "upp/urban_population.csv"
        lab = "Urban population rate"
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
        fin = "../out/multipleRegression_3values.csv"
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
        fin = "../dat/fpi/gdp_per_cap_fpi_st.csv"
        lab = "GDP per cap / Food Price index"
    elif fn == "lor":
        fin = "../out/logisticRegression_guci.csv"
        lab = "Logistic Regression (GDP, UPR, Cor, Gini)"
    elif fn == "sow":
        fin = "../dat/sow/soilmois_cropland_ave_hist.csv"
        lab = "Soil Moisture in cropland (1971 - 2019)"
    elif fn == "sowf":
        fin = "../dat/sow/soilmois_cropland_ave_rcp8p5.csv"
        lab = "Soil Moisture in cropland (RCP8.5, 2005 - 2099)"
    elif fn == "gin":
        fin = "../dat/gin/gini_coeff.csv"
        lab = "Gini Coefficient"
    elif fn == "war":
        fin = "../dat/war/war.csv"
        lab = "War"

    return [fin, lab]


### edit here   #select from aws, gdp, gpi, unr, upp
dataname = "war"
logscale = False
saveflag = False
famcheck = False   ### set True for the past dataset

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
prj = "drgt"
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
    for y in range(1961,2019):
        for i in range(len(dff)):
            cnt = df["ISO3"][i]
            print(cnt)
            if dff.loc[cnt, str(y)] != 0:
                plt.scatter(y, dfp[i][y - syr + 1], color="Red", s=dff.loc[cnt,str(y)] * 5000, alpha=0.5, linewidths=None, zorder=100)

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