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

    return [fin, lab]


### edit here   #select from aws, gdp, gpi, unr, upp
dataname = "uppf"
logscale = False
saveflag = True


### input data
fn = filename(dataname)
df = pd.read_csv("../../dat/"+fn[0])
dfp = df.values
dff = pd.read_csv("../../dat/fam/famineDataNumberRate_drought.csv")
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

print(dff)


#for y in range(1961,2019):
#    for i in range(len(dfp)):
#       cnt = df["ISO3"][i]
#       print(cnt)
#       if dff.loc[cnt, str(y)] != 0:
#           plt.scatter(y-1,dfp[i][y-1961]*100, color="Red", s=dff.loc[cnt,str(y)]*5000, alpha=0.5, linewidths=None, zorder=100)

#plt.scatter(1965, -0.00010*100, color="Red", s=0.01*5000, alpha=0.5, linewidths=None, zorder=100)
#plt.scatter(1965, -0.00015*100, color="Red", s=0.05*5000, alpha=0.5, linewidths=None, zorder=100)
#plt.scatter(1965, -0.00020*100, color="Red", s=0.1*5000, alpha=0.5, linewidths=None, zorder=100)

if logscale:
    plt.yscale("log")

plt.title(fn[1])

if saveflag:
    if dataname=="awspc":
        plt.savefig("../../fig/aws/"+prj+"____"+dataname+".png",dpi=300,bbox_inches="tight")
    elif dataname=="vappc":
        plt.savefig("../../fig/vap/"+prj+"____"+dataname+".png",dpi=300,bbox_inches="tight")
    else:
        plt.savefig("../../fig/"+dataname+"/"+prj+"____"+dataname+".png",dpi=300,bbox_inches="tight")


#plt.savefig("../../fig/multipleRegression_new" + dataname + ".png",dpi=300,bbox_inches="tight")
plt.show()
plt.close()