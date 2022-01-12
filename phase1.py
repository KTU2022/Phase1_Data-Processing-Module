# -*- coding: utf-8 -*-
"""Phase1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ST6Bb1VALpR3NVr9QgZvlkDy2Zmqs5xn

Importing required libraries and loading datasets
"""

import numpy as np
import pandas as pd
import netCDF4 as nc
import matplotlib.pyplot as mp
data1=nc.Dataset('/content/drive/MyDrive/Colab Notebooks/oisst-avhrr-v02r01.20110101.nc')
data2=nc.Dataset('/content/drive/MyDrive/Colab Notebooks/oisst-avhrr-v02r01.20110102.nc')
data3=nc.Dataset('/content/drive/MyDrive/Colab Notebooks/oisst-avhrr-v02r01.20110103.nc')
data4=nc.Dataset('/content/drive/MyDrive/Colab Notebooks/oisst-avhrr-v02r01.20110104.nc')
data5=nc.Dataset('/content/drive/MyDrive/Colab Notebooks/oisst-avhrr-v02r01.20110105.nc')
data6=nc.Dataset('/content/drive/MyDrive/Colab Notebooks/uv20110101.nc')

"""Determining dimension
values existing in the dataset
"""

for d in data1.dimensions.values():
  print(d)
for d in data6.dimensions.values():
  print(d)

"""Extracting multidimensional data from NetCDF file"""

data1.variables.keys()
data6.variables.keys()

lat=data1.variables['lat'][:]
lon=data1.variables['lon'][:]
zl=data1.variables['zlev'][:]
time=data1.variables['time'][:]
sst1=data1.variables['sst'][:]
sst2=data2.variables['sst'][:]
sst3=data3.variables['sst'][:]
sst4=data4.variables['sst'][:]
sst5=data5.variables['sst'][:]
swx=data6.variables['u'][:]
swy=data6.variables['v'][:]
swsp=data6.variables['w'][:]

lat1=[]
lon1=[]
SST1=[]
SST2=[]
SST3=[]
SST4=[]
SST5=[]
swx1=[]
swy1=[]
swsp1=[]
for t in range(len(time)):
  for z in range(len(zl)):
    for i in range(len(lat)-1):
      for j in range(len(lon)-1):
        if(sst1[t,z,i,j]!='--' and sst2[t,z,i,j]!='--' and sst3[t,z,i,j] != '--' and sst4[t,z,i,j] != '--' and swsp[t,z,i,j]!='--' ):
          lat1.append(lat[i])
          lon1.append(lon[j])
          SST1.append(sst1[t,z,i,j])
          SST2.append(sst2[t,z,i,j])
          SST3.append(sst3[t,z,i,j])
          SST4.append(sst4[t,z,i,j])
          SST5.append(sst5[t,z,i,j])
          swsp1.append(swsp[t,z,i,j])

"""Creating
Dictionary dict using
lat1 ,lon1 ,SST1 ,SST2 ,SST3 ,SST4 ,SST5 ,SEAWIND
"""

dict={'Lat':lat1,'Lon':lon1,'SST1':SST1,'SST2':SST2,'SST3':SST3,'SST4':SST4,'SST5':SST5,"WINDSPEED":swsp1}
df=pd.DataFrame(dict)
dd=df
dd.head(20)

"""Time series representation of Sea wind and SST"""

g=mp.figure().gca(projection = '3d')
g.scatter(df['Lat'],df['Lon'],df['WINDSPEED'])
g.scatter(df['Lat'],df['Lon'],df['SST1'])