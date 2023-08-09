# -*- coding: utf-8 -*-
"""
Author=Gaurav Chopra
"""
# import os
# os.environ['PROJ_LIB'] = r'/home/gchopra/anaconda3/pkgs/proj4-5.2.0-h295c915_1001/share/proj'


from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
#import scipy.stats as scipy
#import networkx as nx

year = np.linspace(1990,2020,31)

for i in year:
    my_file= str('precip-' + str(year) + '.nc')
    
    
    fh = Dataset(my_file, mode='r')
    
    lons = fh.variables['longitude'][:]
    lats=fh.variables['latitude'][:]
    olrdata=fh.variables['tp'][:]*-1.0
    olrdata_units=fh.variables['tp'].units
    fh.close()
    print("Files read")
    
    dimlat=len(lats)
    dimlon=len(lons)
    k=0
        
    '''
    Developing Transformed Matrix
    '''
    
    dimlat=0
    dimlon=0
    k=0
    step=5
    for lati in range(0,len(lats),step):
        dimlat=dimlat+1
        dimlon=0
        for loni in range(0,len(lons),step):
            dimlon=dimlon+1
            k=k+1
    
    print(k)
    print(dimlat)
    print(dimlon)
    
    
    
    dim1=int(len(olrdata))
    print("Time,:",dim1)
    dim2=k
    tran_data_olr=np.zeros((dim1,dim2),dtype=np.float64)
    modlat=np.zeros((dimlat),dtype=np.float32)
    modlon=np.zeros((dimlon),dtype=np.float32)
    
    dimlat=0
    
    
    for lati in range(0,len(lats),step):
        modlat[dimlat]=lats[lati]
        dimlat=dimlat+1
    
    dimlon=0    
    for loni in range(0,len(lons),step):
        modlon[dimlon]=lons[loni]
        dimlon=dimlon+1
        
    k=0
    for lati in range(0,len(lats),step):
        for loni in range(0,len(lons),step):
            t=0
            for timei in range(0,dim1):
                tran_data_olr[t,k]=olrdata[timei,lati,loni]
                t=t+1
            k=k+1
    print(k)
    
    np.savetxt('precip'+ str(year) + '.dat',tran_data_olr,fmt='%1.4e')
    
    np.savetxt('modlat.dat',modlat,fmt='%1.4e')
    np.savetxt('modlon.dat',modlon,fmt='%1.4e')
    
    
    
    
    



