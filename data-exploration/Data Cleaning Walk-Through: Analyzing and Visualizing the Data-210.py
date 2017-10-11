## 3. Finding Correlations With the r Value ##

correlations = combined.corr() 
print(correlations["sat_score"])

## 5. Plotting Enrollment With the Plot() Accessor ##

import matplotlib.pyplot as plt
combined.plot.scatter(x='total_enrollment', y='sat_score')
plt.show()

## 6. Exploring Schools With Low SAT Scores and Enrollment ##

low_enrollment = combined[combined["total_enrollment"] < 1000] 
low_enrollment = combined[combined["sat_score"] < 1000] 
print(low_enrollment["School Name"])

## 7. Plotting Language Learning Percentage ##

combined.plot.scatter(x = "ell_percent", y = "sat_score")
plt.show()

## 9. Mapping the Schools With Basemap ##

from mpl_toolkits.basemap import Basemap

longitudes = combined["lon"].tolist()
latitudes= combined["lat"].tolist()

m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.scatter(longitudes,latitudes,s=20,zorder=2,latlon=True)
m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

plt.show() 

## 10. Plotting Out Statistics ##

from mpl_toolkits.basemap import Basemap

longitudes = combined["lon"].tolist()
latitudes= combined["lat"].tolist()

m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.scatter(longitudes,latitudes,s=20,zorder=2,latlon=True,c = combined["ell_percent"],cmap="summer")
m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

plt.show() 

## 11. Calculating District-Level Statistics ##

import numpy 
grouped = combined.groupby("school_dist")
districts = grouped.agg(numpy.mean)
districts.reset_index(inplace=True)
print(districts.head())


## 12. Plotting Percent Of English Learners by District ##

from mpl_toolkits.basemap import Basemap

longitudes = districts["lon"].tolist()
latitudes= districts["lat"].tolist()

m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.scatter(longitudes,latitudes,s=50,zorder=2,latlon=True,c = districts["ell_percent"],cmap="summer")

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

plt.show() 