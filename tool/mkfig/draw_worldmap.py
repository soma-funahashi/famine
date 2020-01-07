###########################################################
#to          : template for drawing world map
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/10/15
###########################################################

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader

def area(ax, iso, clr) :
    shp = shpreader.natural_earth(resolution='50m',category='cultural',
                                  name='admin_0_countries')
    reader = shpreader.Reader(shp)
    for n in reader.records():
        print(n.attributes['NAME_EN'],n.attributes['ISO_A3'])
        if n.attributes['ISO_A3'] == iso: 
            ax.add_geometries(n.geometry, ccrs.PlateCarree(), facecolor=clr, 
                              alpha = 1.00, linewidth =0.15, edgecolor = "black",
                              label=n.attributes['ISO_A3']) 
    return ax

iso3 = ['SSD']

plt.figure()
countries_50m  = cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='gray', facecolor='none', linewidth=0.1)
ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.outline_patch.set_linewidth(1)
ax.set_extent([-30, 90, -60, 60], ccrs.PlateCarree())
ax.coastlines(resolution='50m', linewidth=0.5)
ax.add_feature(countries_50m)

for n in iso3 :
    area(ax, n, "red")
plt.savefig("test2.png")
plt.show()
