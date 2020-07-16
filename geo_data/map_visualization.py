#!/usr/bin/env python
# coding: utf-8

# # Visualize geographical data on map
# 
# Geographical data can be visualized using GeoPandas https://geopandas.org and Folium https://python-visualization.github.io/folium/, which allows the interactive visualization of data on a map from OpenStreetMap https://www.openstreetmap.org.

# ###### Python 3.7
# 
# General packages: numpy, matplotlib
# 
# ###### Installation instructions for specifically required packages
# 
#     conda install geopandas    
#     pip install folium

# ##### Example data
# 
# Example data can be downloaded from https://data.geo.admin.ch. The specific dataset used here is  http://data.geo.admin.ch.s3.amazonaws.com/ch.swisstopo.swissboundaries3d-kanton-flaeche.fill/data.zip. 
# 
# The shape data from that source can be converted to geoson as follows:
# 
#   ogr2ogr -f GeoJSON -t_srs EPSG:4326 -simplify 1000 switzerland.geojson swissBOUNDARIES3D_1_2_TLM_KANTONSGEBIET.shp
#   
# The tool 'ogr2ogr' is part of the GDAL-package https://pypi.org/project/GDAL/ which is already installed as a dependency of geopandas.

# #### First import all required modules

# In[1]:


import folium
print (folium.__version__)


# In[2]:


import geopandas as gpd


# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import numpy as np


# ## Simple map using Matplotlib and GeoPandas

# In[5]:


# Read Geojson-file
df = gpd.read_file('switzerland.geojson')
print (df.columns)
df.head()


# In[6]:


# basic map plot
fig, ax = plt.subplots(figsize=(20,20))
df.plot(ax=ax, column='ERSTELL_J', cmap='OrRd', edgecolor='black')


# ### Visualize data on simple map

# In[7]:


# basic map plot
fig, ax = plt.subplots(figsize=(20,20))
df.plot(ax=ax, column='EINWOHNERZ', cmap='OrRd', edgecolor='black')


# In[8]:


# Calculate population density using data from GeoJson file
df['density'] = df.EINWOHNERZ / df.KANTONSFLA # calculate population density


# In[9]:


# Visualize population density
fig, ax = plt.subplots(figsize=(20,20))
df.plot(ax=ax, column='density', cmap='OrRd', edgecolor='black')


# ## Interactive map from OpenStreetMap 
# 
# First we look at the map of openstreet map and choose different centers and zoom levels

# In[10]:


# World map: map centered at [0,0, Zoom=1]
kanton_map = folium.Map(location=[0,0],  zoom_start=1)
kanton_map


# In[11]:


# Map of Switzerland and some neighboring countries:
kanton_map = folium.Map(location=[46.8, 8.33],  zoom_start=7)
kanton_map


# In[12]:


# combine map with shape file downloaded before
kanton_map.choropleth(geo_data ='switzerland.geojson', fill_color='white')
kanton_map


# ### Visualize data on interactive map
# 
# Visualize all peaks on canton borders above 3000 m

# In[13]:


# define altitude limit
alt_lim = 3000


# In[14]:


# create peak list
peaks = list()
for kanton in df.index:
    arr = np.array(df.geometry[kanton].exterior.coords)
    peaks.append(arr[np.where(arr[:,2]>alt_lim)].tolist())
peaks = [item for sublist in peaks for item in sublist] # flatten to a single list of 3d points 
print ('number of peaks found = ', len(peaks))


# In[15]:


kanton_map2 = folium.Map(location=[46.8, 8.33], zoom_start=7.5)
feature_group = folium.FeatureGroup("Locations")
for peak in peaks:
    feature_group.add_child(folium.Marker(location=[peak[1], peak[0]], popup=str(peak[2]))) 
kanton_map2.add_child(feature_group)
kanton_map2


# In[ ]:




