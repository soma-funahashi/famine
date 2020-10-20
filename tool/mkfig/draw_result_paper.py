import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize
import matplotlib.colors as colors
from matplotlib.cm import ScalarMappable
import seaborn as sns; sns.set()


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
    elif fn == "5yrs":
        fin = "../out/dflt__rslt__5yrs__cnt.csv"
        lab = "Famine valunerable countries (1961 - 2015)"
    elif fn == "sow":
        fin = "../dat/sow/soilmois_cropland_kg.csv"
        lab = "Soil Moisture in cropland(kg per m2, 1961-2014)"
    elif fn == "sowf":
        fin = "../dat/sow/soilmois_cropland_ave_hist.csv"
        lab = "Soil Moisture in cropland(kg per m2, 1971-2004)"
    elif fn == "gin":
        fin = "../dat/gin/gini_coeff_ave.csv"
        lab = "Gini Coefficient (ave. 1960 - 2019)"

    elif fn == "ssp1":
        fin = "../out/logisticRegression_all_future_ssp1_ave.csv"
        lab = "Logistic Regression (probability, SSP1)"
    elif fn == "ssp2":
        fin = "../out/logisticRegression_all_future_ssp2_ave.csv"
        lab = "Logistic Regression (probability, SSP2)"
    elif fn == "ssp3":
        fin = "../out/logisticRegression_all_future_ssp3_ave.csv"
        lab = "Logistic Regression (probability, SSP3)"


    elif fn == "fam":
        fin = "fam/famineData.csv"
        lab = "Years of famine (1960 - 2019)"
    elif fn == "war":
        fin = "../dat/war/war_bool.csv"
        lab = "Number of years when war happend (1940-2019)"
    elif fn == "fpr":
        fin = "../dat/fpr/cereal_import_dependency.csv"
        lab = "Cereal import dependency (%, 2001-2016)"
    elif fn == "lor":
        fin = "../out/logisticRegression_all.csv"
        lab = "Logistic Regression (prob. 2014)"
    elif fn == "lorf":
        fin = "../out/logisticRegression_all_future_ssp1_rcp4p5.csv"
        lab = "Logistic Regression (prob. 2030, SSP1)"
    elif fn == "pdi":
        fin = "../dat/pdi/mod3_pdsi.csv"
        lab = "Palmer's Drought Severity Index (1961 - 2018)"

    return [fin, lab]




def area(ax, iso, clr):    ### coloring function
    shp = shpreader.natural_earth(resolution='50m',category='cultural',
                                  name='admin_0_countries')
    reader = shpreader.Reader(shp)
    for n in reader.records():
        if n.attributes['ISO_A3'] == iso: 
            ax.add_geometries(n.geometry, ccrs.PlateCarree(), facecolor=clr, 
                              alpha = 1.00, linewidth =0.15, edgecolor = "black",
                              label=n.attributes['ISO_A3']) 
    return ax


fig=plt.figure(figsize=(12,9))


def drawfig(ssp, idx, year):    ### drawing figure
    ### edit here   (select from aws, gdp, gpi, unr, upp)
    dataname = ssp
    logscale = False
    color = "Oranges"

    ### input data
    fn = filename(dataname)
    df = pd.read_csv("../../dat/"+fn[0])
    df = df.fillna(0)
    iso3 = df["ISO3"]

    fam = pd.read_csv("../../dat/fam/famineData_all.csv")
    fam_mean = fam.sum(axis = 1)

    #mx = data.max()
    mx = 0.35
    #mn = data.min()
    mn = 0.00



    data=df[str(year)]

    countries_50m  = cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='gray', facecolor='none', linewidth=0.1)
    ax = plt.subplot(3, 4, idx, projection=ccrs.PlateCarree())
    ax.outline_patch.set_linewidth(1)
    ax.set_extent([-30, 60, -45, 45], ccrs.PlateCarree())
    ax.coastlines(resolution='50m', linewidth=0.5)
    ax.add_feature(countries_50m)
    ax.set_title(str(ssp)+", "+str(year))

    ### setting colormap
    cmap=plt.get_cmap(color)
    if logscale:
        norm = colors.SymLogNorm(linthresh=1.1, linscale=1.1, vmin=0, vmax=mx)
    else:
        norm = Normalize(vmin=mn, vmax=mx)
    mappable = ScalarMappable(cmap=cmap, norm=norm)
    mappable._A = []
    cax = fig.colorbar(mappable)
    for i in range(len(iso3)):
        n=iso3[i]
        if fam_mean[i] > 0:
            if logscale:
                area(ax, n, cmap(np.log(float(data[i]))/np.log(mx)))
            else: 
                area(ax, n, cmap(float(data[i])/mx))
        else:
            if logscale:
                area(ax, n, cmap(np.log(float(data[i]))/np.log(mx)))
            else: 
                area(ax, n, cmap(float(data[i])/mx))

    ax_pos = ax.get_position()
    cax_pos0 = cax.ax.get_position()
    cax_pos1 = [cax_pos0.x0, ax_pos.y0, cax_pos0.x1 - cax_pos0.x0, ax_pos.y1 - ax_pos.y0]
    cax.ax.set_position(cax_pos1)

drawfig("ssp1", 1, 2021)
drawfig("ssp1", 2, 2030)
drawfig("ssp1", 3, 2040)
drawfig("ssp1", 4, 2050)

drawfig("ssp2", 5, 2021)
drawfig("ssp2", 6, 2030)
drawfig("ssp2", 7, 2040)
drawfig("ssp2", 8, 2050)

drawfig("ssp3", 9, 2021)
drawfig("ssp3", 10, 2030)
drawfig("ssp3", 11, 2040)
drawfig("ssp3", 12, 2050)

# plt.subplots_adjust(wspace=0, hspace=0)
plt.savefig("../../fig/plt/map_paper_future.png", dpi=300, bbox_inches="tight")
plt.show()