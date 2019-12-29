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
        fin = "../out/multipleRegression.csv"
        lab = "Estimated death rate by famine (% of the population)"
    elif fn == "out2":
        fin = "../out/multipleRegression_4values.csv"
        lab = "Estimated death rate by famine (% of the population)"

    return [fin, lab]


### edit here   #select from aws, gdp, gpi, unr, upp
dataname = "out2"
logscale = False
saveflag = True


### input data
fn = filename(dataname)
df = pd.read_csv("../../dat/"+fn[0])
dfp = df.values
dff = pd.read_csv("../../dat/fam/famineDataNumberRate.csv")
dfg = pd.read_csv("../../dat/gpi/global_peace_index_filled.csv")
fam = pd.read_csv("../../dat/fam/famineData.csv")
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
df3 = pd.read_csv("../../out/"+prj+"____vald.csv")
val = df3["Result"]

plt.figure(figsize=(8,6))

for i in range(1,len(dfp)):
    tmp = dfp[i][1:]
    tmp = tmp.astype("float32")
    if fam[i]>=1:
        plt.plot(yl, tmp*100, linewidth=0.5, color="red",zorder=50)
        print(df3["ISO3"][i])
    elif gpi[i]>2.9 or cor[i]>0.2:
        plt.plot(yl, tmp*100, linewidth=0.5, color="lightgray")
    else:
        plt.plot(yl, tmp*100, linewidth=0.5, color="lightgray")


for y in range(1961,2012):
    for i in range(len(dfp)):
        if dff[str(y)][i]>0:
            plt.scatter(y,dfp[i][y-1961]*100, color="Red", s=dff[str(y)][i]*500, alpha=0.5, linewidths=None, zorder=100)

# plt.scatter(1965, -0.0015*100, color="Red", s=0.01*500, alpha=0.5, linewidths=None, zorder=100)
# plt.scatter(1965, -0.00175*100, color="Red", s=0.05*500, alpha=0.5, linewidths=None, zorder=100)
# plt.scatter(1965, -0.002*100, color="Red", s=0.1*500, alpha=0.5, linewidths=None, zorder=100)

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

plt.show()
plt.close()