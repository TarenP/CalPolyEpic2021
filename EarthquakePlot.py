import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import matplotlib.lines as mlines


#Establish earthquake & map data for plot
EQdata=pd.read_csv('USGS_M5plus_2000later.csv')
print(EQdata.head())

gdf = gpd.GeoDataFrame(EQdata, geometry=gpd.points_from_xy(EQdata.longitude, EQdata.latitude))

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

size=(3**(EQdata.mag))/ 30

ax = world[world.continent == 'North America'].plot(color='white', edgecolor='black')

colortype=[]
for i in range(0,len(EQdata)):
  if EQdata.mag[i]<5.5:
    colortype.append('lightgrey')
  elif EQdata.mag[i]<6:
    colortype.append('orange')
  elif EQdata.mag[i]<6.5:
    colortype.append('darkorange')
  elif EQdata.mag[i]<7:
    colortype.append('red')
  else:
    colortype.append('darkred')


mag55 = mlines.Line2D([], [], color='lightgrey', alpha=0.5, marker='o', linestyle='None', markersize=(2**6.1)/15, label='0-5.5')
mag6 = mlines.Line2D([], [], color='orange', alpha=0.3, marker='o', linestyle='None', markersize=(2**6.3)/15, label='5.5-6')
mag65 = mlines.Line2D([], [], color='darkorange', alpha=0.4, marker='o', linestyle='None', markersize=(2**6.5)/15, label='6-6.5')
mag7 = mlines.Line2D([], [], color='red', alpha=0.3, marker='o', linestyle='None', markersize=(2**6.7)/15, label='6.5-7')
mag75 = mlines.Line2D([], [], color='darkred', alpha=0.3, marker='o', linestyle='None', markersize=(2**7)/15, label='7+')
plt.legend(handles=[mag55,mag6,mag65,mag7,mag75],title='Magnitude',bbox_to_anchor=(0.5, -0.15), loc='upper center',ncol=5)


gdf.plot(ax=ax, color=colortype,markersize=size,alpha=0.2)
plt.savefig('EQFigure.png')

plt.show()
