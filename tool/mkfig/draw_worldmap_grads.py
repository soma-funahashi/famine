import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize
import matplotlib.colors as colors
from matplotlib.cm import ScalarMappable


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

### edit here   (select from aws, gdp, gpi, unr, upp)
dataname = "gdp"
logscale = True
saveflag = False
color = "Blues"

### input data
fn = filename(dataname)
df = pd.read_csv("../../dat/"+fn[0])
df=df.fillna(0)
iso3=df["ISO3"]

### get average
data=df.mean(axis="columns")
fn_out=fn[1]
m = data.max()

def area(ax, iso, clr):    ### coloring function
    shp = shpreader.natural_earth(resolution='50m',category='cultural',
                                  name='admin_0_countries')
    reader = shpreader.Reader(shp)
    for n in reader.records() :
        if n.attributes['ISO_A3'] == iso: 
            ax.add_geometries(n.geometry, ccrs.PlateCarree(), facecolor=clr, 
                              alpha = 1.00, linewidth =0.15, edgecolor = "black",
                              label=n.attributes['ISO_A3']) 
    return ax


def fig():    ### drawing figure
    fig=plt.figure(figsize=(10,6))
    countries_50m  = cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='gray', facecolor='none', linewidth=0.1)
    ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.outline_patch.set_linewidth(1)
    ax.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
    ax.coastlines(resolution='50m', linewidth=0.5)
    ax.add_feature(countries_50m)
    ax.set_title(fn_out)

    ### setting colormap
    cmap=plt.get_cmap(color)
    if logscale:
        norm = colors.SymLogNorm(linthresh=1.1, linscale=1.1, vmin=0, vmax=m)
    else:
        norm = Normalize(vmin=0, vmax=m)
    mappable = ScalarMappable(cmap=cmap, norm=norm)
    mappable._A = []
    cax = fig.colorbar(mappable)
    for i in range(len(iso3)):
        n=iso3[i]
        if logscale:
            area(ax, n, cmap(np.log(float(data[i]))/np.log(m)))
        else: 
            area(ax, n, cmap(float(data[i])/m))

    ax_pos = ax.get_position()
    cax_pos0 = cax.ax.get_position()
    cax_pos1 = [cax_pos0.x0, ax_pos.y0, cax_pos0.x1 - cax_pos0.x0, ax_pos.y1 - ax_pos.y0]
    cax.ax.set_position(cax_pos1)
    if saveflag:
        plt.savefig("../../fig/"+dataname+"/"+fn_out+".png", dpi=300, bbox_inches="tight")
    plt.show()

fig()
