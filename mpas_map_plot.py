
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.animation as animation
import numpy as np
import xarray as xr
from matplotlib import pyplot as plt

import matplotlib.colors as wa

import cartopy.mpl.ticker as cticker

ds1 = xr.open_dataset("/Users/alan/Desktop/files/data/MPAS/hr_500hpa.nc", decode_times=False)

fe="9"
it=8

tas1 = ds1.relhum_500hPa[it,:,:]


#########################################################################################################################3
#colorbar
paleta2=wa.LinearSegmentedColormap.from_list("custom",["white","skyblue","deepskyblue","cornflowerblue","lightgreen",
                                              "limegreen","orange","darkorange","orchid","darkorchid"])

##########################################################################################################################


######################################################################
################### Plot the variable ################################

# Define the figure object and primary axes
fig, ax = plt.subplots(figsize=(20, 14), subplot_kw={'projection': ccrs.PlateCarree()})



# set the spacing between subplots
#For Australia
cod=[0.05,0.05,0.95,0.4,0.2,0.]
plt.subplots_adjust(left=cod[0],
                    bottom=cod[1],
                    right=cod[2],
                    top=cod[3],
                    wspace=cod[4],
                    hspace=cod[5])




##########################################################################################################################
#Define the contour

#it=[5,10,12,15,20,30,40,50,60,70,80]

it=[0,1,5,10,15,20,30,40,50,60,70]

#it=[0,.1,.5,1,2,3,4,5,6,7,8]



#Change the order of the dimensions

plot1 = ax.contourf(tas1['longitude'], tas1['latitude'], tas1, levels=it,   #levels=np.arange(2, 101, 2)
                                                             cmap=paleta2 , extend='max')    #'Blues'

# Longitude labels
ax.set_xticks(np.arange(-180,181,30), crs=ccrs.PlateCarree())
lon_formatter = cticker.LongitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)

# Latitude labels
ax.set_yticks(np.arange(-90,91,15), crs=ccrs.PlateCarree())
lat_formatter = cticker.LatitudeFormatter()
ax.yaxis.set_major_formatter(lat_formatter)

# Title each subplot with the name of the model
#ax[i].set_title(model[i])

#-- add coastlines, country border lines, and grid lines
ax.coastlines(linewidths=0.9)  #0.5


country_borders = cfeature.NaturalEarthFeature(
category='cultural',
name='admin_0_boundary_lines_land',
scale='50m',
facecolor='none')
ax.add_feature(country_borders, edgecolor='gray')


cbar = plt.colorbar(plot1, ax=ax, orientation='vertical', shrink=0.7, pad=0.05)
cbar.set_label('Relhum 500 hPa')  # Cambia la etiqueta según corresponda




plt.savefig("/Users/alan/Desktop/files/scripts/python/figures/mundo"+fe+".png")