from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

modlat = np.loadtxt('modlat.dat')
modlon = np.loadtxt('modlon.dat')

dimlat, dimlon = len(modlat), len(modlon)

raw_data = np.loadtxt('trans_data_olr_day_avg.dat')
time4 = np.loadtxt('timescale-4.txt')

data = raw_data[567,:] #datat manipulation

dimcn=len(data)
mod_data=np.zeros((dimlat,dimlon),dtype=np.float64)

k=0
for lati in range (0,dimlat):
    for loni in range (0,dimlon):
        mod_data[lati,loni]=data[k]
        k=k+1

m = Basemap(projection='merc',llcrnrlat=-23.5,urcrnrlat=23.5,\
        llcrnrlon=-180,urcrnrlon=180,lat_ts=5,resolution='i')

lon, lat = np.meshgrid(modlon,modlat)
xi, yi = m(lon, lat)

fig=plt.figure(figsize=(15,10))
ax=plt.axes()
cs = m.contourf(xi,yi,mod_data,cmap='RdBu_r',extend='both')


# Add Grid Lines
m.drawparallels(np.arange(-23.5,23.5,10), labels=[1,0,0,0], fontsize=15)
m.drawmeridians(np.arange(-180,180, 30.), labels=[0,0,0,1], fontsize=15)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
#m.drawstates()
#m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="50%",format='%3.0f')
cbar.ax.tick_params(labelsize=15)


# Add Title
plt.xlabel("Longitude $(^o)$",fontsize=20,labelpad=30)
plt.ylabel("Latitude $(^o)$",fontsize=20,labelpad=60)
plt.title("Outgoing Longwave Radiation ",fontsize=20,pad=20)
plt.savefig('raw.jpeg')

data2 = time4[567,:] #datat manipulation

dimcn=len(data2)
mod_data=np.zeros((dimlat,dimlon),dtype=np.float64)

k=0
for lati in range (0,dimlat):
    for loni in range (0,dimlon):
        mod_data[lati,loni]=data2[k]
        k=k+1

m = Basemap(projection='merc',llcrnrlat=-23.5,urcrnrlat=23.5,\
        llcrnrlon=-180,urcrnrlon=180,lat_ts=5,resolution='i')

lon, lat = np.meshgrid(modlon,modlat)
xi, yi = m(lon, lat)
fig=plt.figure(figsize=(15,10))
ax=plt.axes()
cs = m.contourf(xi,yi,mod_data,cmap='RdBu_r',extend='both')


# Add Grid Lines
m.drawparallels(np.arange(-23.5,23.5,10), labels=[1,0,0,0], fontsize=15)
m.drawmeridians(np.arange(-180,180, 30.), labels=[0,0,0,1], fontsize=15)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
#m.drawstates()
#m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="50%",format='%3.0f')
cbar.ax.tick_params(labelsize=15)


# Add Title
plt.xlabel("Longitude $(^o)$",fontsize=20,labelpad=30)
plt.ylabel("Latitude $(^o)$",fontsize=20,labelpad=60)
plt.title("Outgoing Longwave Radiation ",fontsize=20,pad=20)
plt.savefig('timescale4.jpeg')
