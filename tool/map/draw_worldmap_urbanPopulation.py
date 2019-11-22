import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import sys

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

### input data
df=pd.read_csv("../../dat/upp/urban_population.csv")
df=df.fillna(0)
iso3=df["ISO3"]

### set year
s=sys.argv
year=s[1]
data=df[str(year)]
fn_out="urbanPopulation_"+str(year)+".png"

### collecting dataset
m=0
for y in range(1961,2011):
    tmp=max(df[str(y)])
    m=max(tmp,m)

### drawing figure
fig=plt.figure(figsize=(10,6))
countries_50m  = cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='gray', facecolor='none', linewidth=0.1)
ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.outline_patch.set_linewidth(1)
ax.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
ax.coastlines(resolution='50m', linewidth=0.5)
ax.add_feature(countries_50m)
ax.set_title("Urban Population Rate in "+str(year)+" (FAO,2011)")

### setting colormap
cmap=plt.get_cmap("OrRd")
norm = Normalize(vmin=0, vmax=m)
mappable = ScalarMappable(cmap=cmap, norm=norm)
mappable._A = []
cax = fig.colorbar(mappable)

for i in range(len(iso3)):
    n=iso3[i]
    area(ax, n, cmap(float(df[str(year)][i])/m))

ax_pos = ax.get_position()
cax_pos0 = cax.ax.get_position()
cax_pos1 = [cax_pos0.x0, ax_pos.y0, cax_pos0.x1 - cax_pos0.x0, ax_pos.y1 - ax_pos.y0]
cax.ax.set_position(cax_pos1)


plt.show()
#plt.savefig("../fig/urban_population/"+fn_out,bbox_inches="tight")
