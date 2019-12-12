###########################################################
#to          : template for drawing world map
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/10/15
###########################################################

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import pandas as pd


def area(ax, iso, clr) :
    shp = shpreader.natural_earth(resolution='50m',category='cultural',
                                  name='admin_0_countries')
    reader = shpreader.Reader(shp)
    for n in reader.records() :
        if n.attributes['ADM0_A3'] == iso: 
            ax.add_geometries(n.geometry, ccrs.PlateCarree(), facecolor=clr, 
                              alpha = 1.00, linewidth =0.15, edgecolor = "black",
                              label=n.attributes['ADM0_A3']) 
    return ax

#iso3 = ['USA','CAN','RUS','GBR','ISL','FRA','ITA','CHN','AUT','JPN']

### input

def validation():
    plt.figure()
    countries_50m  = cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='gray', facecolor='none', linewidth=0.1)
    ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.outline_patch.set_linewidth(1)
    ax.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
    ax.coastlines(resolution='50m', linewidth=0.5)
    ax.add_feature(countries_50m)
    ax.set_title('Difference of Correlation Coefficient')

    for i in range(len(dfo["ISO3"])):
        n = dfo["ISO3"][i]
        if dfo["cor"][i] == 1 and dfs["cor"][i] >= 0.15:
            area(ax, n, "limegreen")
        elif dfo["cor"][i] == 1 and dfs["cor"][i] <= 0.15:
            area(ax, n, "royalblue")
        elif dfo["cor"][i] == 0 and dfs["cor"][i] >= 0.15:
            area(ax, n, "gold")
    plt.savefig("../../fig/cor/correlation_diff.png", dpi=300, bbox_inches="tight")
    plt.show()


dfo = pd.read_csv("../../dat/cor/correlation.csv")
dfs = pd.read_csv("../../dat/cor/correlation_data.csv")

validation()
