# Wrote this code to plot the first observation of nodes of different timescales decomposed
# using MODWT
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

print('Importing modlat')
modlat = np.loadtxt('../modlat.dat')
print('Importing modlon')
modlon = np.loadtxt('../modlon.dat')

dimlat, dimlon = len(modlat), len(modlon)


for scale in range(0,10):
    file_path = 'timescale' + str(scale) + '/combine-timescale-' + str(scale) + '.txt'
    print('Importing file: ', file_path)
    data = np.genfromtxt(file_path, delimiter = ' ', max_rows = 1)

    dimcn=len(data)
    print('Mapping...')
    mod_data=np.zeros((dimlat,dimlon),dtype=np.float64)

    k=0
    for lati in range (0,dimlat):
        for loni in range (0,dimlon):
            mod_data[lati,loni]=data[k]
            k=k+1

    m = Basemap(projection='merc', llcrnrlat=-23.5, urcrnrlat=23.5, llcrnrlon=-180, urcrnrlon=180, lat_ts=5, resolution = 'i')

    lon, lat = np.meshgrid(modlon,modlat)
    xi, yi = m(lon, lat)

    fig = plt.figure(figsize=(15,5))
    ax = plt.axes()
    vmin, vmax = 0, 350
    cs = m.contourf(xi, yi, mod_data,cmap='RdBu_r',extend='both', levels = np.linspace(vmin, vmax, 150))

    print('Plotting...')
    # Add Grid Lines
    m.drawparallels(np.arange(-23.5,23.5,10), labels=[1,0,0,0], fontsize=15)
    m.drawmeridians(np.arange(-180,180, 30.), labels=[0,0,0,1], fontsize=15)

    # Add Coastlines, States, and Country Boundaries
    m.drawcoastlines()
    #m.drawstates()

    cbar = m.colorbar(cs, location='bottom', pad="50%",format='%3.0f')
    cbar.ax.tick_params(labelsize = 15)
    cbar.set_ticks(range(vmin, vmax, 50))

    # Add Title
    plt.xlabel("Longitude $(^o)$",fontsize=14,labelpad=30)
    plt.ylabel("Latitude $(^o)$",fontsize=14,labelpad=60)
    plt.title("Outgoing Longwave Radiation ",fontsize=16,pad=20)
    save_path = 'node1-timescale' + str(scale) + '.jpeg'
    print('Saving file: ', save_path)
    plt.savefig(save_path)

