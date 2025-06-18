

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.animation as animation
import numpy as np
import xarray as xr
from matplotlib import pyplot as plt

import matplotlib.colors as wa

import cartopy.mpl.ticker as cticker

# Load dataset
ds1 = xr.open_dataset("/home/agarciar/Desktop/files/data/var_850hpa.nc", decode_times=False)

# Define the time indices you want to plot (4 for 2x2)
time_indices = [3, 5, 7, 8]

# Define the contour levels
#levels = [0,1,5,10,15,20,30,40,50,60,70]

levels = [0,1,5,10,15,20,30,40]


# Define colormap
paleta2 = wa.LinearSegmentedColormap.from_list("custom", ["white","skyblue","deepskyblue","cornflowerblue",
                                                         "lightgreen","limegreen","orange","darkorange",
                                                         "orchid","darkorchid"])

# Create figure and axes (2x2) with Cartopy projection
fig, axes = plt.subplots(2, 2, figsize=(20, 14),
                         subplot_kw={'projection': ccrs.PlateCarree()})

# Flatten axes array for easy iteration
axes = axes.flatten()

for i, it in enumerate(time_indices):
    ax = axes[i]
    # Extract data for the current time index
    hum = ds1.temperature_850hPa[it,:,:]-273.15

    # Plot filled contours
    cf = ax.contourf(hum['longitude'], hum['latitude'], hum, levels=levels,
                     cmap=paleta2, extend='max')

    # Add coastlines and borders
    ax.coastlines(linewidth=0.9)
    country_borders = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_0_boundary_lines_land',
        scale='50m',
        facecolor='none')
    ax.add_feature(country_borders, edgecolor='gray')

    # Set ticks and formatters
    ax.set_xticks(np.arange(-180, 181, 60), crs=ccrs.PlateCarree())
    ax.set_yticks(np.arange(-90, 91, 30), crs=ccrs.PlateCarree())
    ax.xaxis.set_major_formatter(cticker.LongitudeFormatter())
    ax.yaxis.set_major_formatter(cticker.LatitudeFormatter())

    # Add title for each subplot
    ax.set_title(f"Relhum 850 hPa, time index {it}")

# Adjust layout to prevent overlap
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.05, wspace=0.15, hspace=0.15)

# Add a single colorbar for all subplots
cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])  # [left, bottom, width, height]
fig.colorbar(cf, cax=cbar_ax, orientation='vertical', label='Relhum 850 hPa')

plt.show()