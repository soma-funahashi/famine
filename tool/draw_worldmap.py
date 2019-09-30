import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader

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

iso3 = ['USA','CAN','RUS','GBR','ISL','FRA','ITA','CHN','AUT','JPN']

plt.figure()
countries_50m  = cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='gray', facecolor='none', linewidth=0.1)
ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.outline_patch.set_linewidth(1)
ax.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
ax.coastlines(resolution='50m', linewidth=0.5)
ax.add_feature(countries_50m)
ax.set_title('countries_border')

for n in iso3 :
    area(ax, n, "red")

plt.show()
