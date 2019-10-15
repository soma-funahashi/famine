###########################################################
#to          : draw a map of validation result
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/10/15
###########################################################
import matplotlib.pyplot as plt
import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader

### setting
prj="dflt"                                            # project name (4 letters)

### input data
dfv = pd.read_csv("../out/" + prj + "____vald.csv")   # validation data
dfv = dfv.fillna(0)

### coloring function
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


def validation():
    plt.figure()
    countries_50m  = cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='gray', facecolor='none', linewidth=0.1)
    ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.outline_patch.set_linewidth(1)
    ax.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
    ax.coastlines(resolution='50m', linewidth=0.5)
    ax.add_feature(countries_50m)
    ax.set_title(prj+' : validation result')

    for i in range(len(dfv["ISO3"])):
        n = dfv["ISO3"][i]
        if dfv["Result"][i] == "b":
            area(ax, n, "darkorchid")
        elif dfv["Result"][i] == "m":
            area(ax, n, "tomato")
        elif dfv["Result"][i] == "o":
            area(ax, n, "royalblue")
    plt.savefig("../fig/validation/"+prj+"____vald.png", bbox_inches="tight")
    plt.show()

def phase():
    plt.figure()
    countries_50m  = cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='gray', facecolor='none', linewidth=0.1)
    ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.outline_patch.set_linewidth(1)
    ax.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
    ax.coastlines(resolution='50m', linewidth=0.5)
    ax.add_feature(countries_50m)
    ax.set_title('Validation result')

    for i in range(len(dfv["ISO3"])):
        n = dfv["ISO3"][i]
        if dfv["Result"][i] == "o" and dfv["Phase"][i] == 3:
            area(ax, n, "#009F8C")
        elif dfv["Result"][i] == "o" and dfv["Phase"][i] == 2:
            area(ax, n, "#40BFB0")
        elif dfv["Result"][i] == "o" and dfv["Phase"][i] == 1:
            area(ax, n, "#C8EFEA")

    plt.show()


validation()
#phase()
