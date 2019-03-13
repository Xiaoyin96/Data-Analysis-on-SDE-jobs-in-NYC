

import pandas as pd
import numpy as np


from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
df = pd.read_csv('NYC_Jobs.csv')
data_v1 = df.drop(columns = ['Job ID','Posting Date','Posting Updated','Process Date','Agency','Level','Civil Service Title'])
df2 = data_v1[data_v1['Job Category'].str.contains('Data|Technology|data').replace(np.nan, False, regex=True)]
df2 = df2.reset_index(drop = True)

def geocodeN(address):
    gps=Nominatim(user_agent="s4yu@ucsd.edu")
    try:
        location = gps.geocode(address,timeout = 10)
    except GeocoderTimedOut as e:
        print("Error: geocode failed on input %s "%(address))
    #location=gps.geocode(address, timeout = 10)
    return location.longitude,location.latitude

'''--------------------------Salary normalization------------------------------'''
df2['Salary'] = df2[['Salary Range From','Salary Range To']].mean(axis=1) 

for i in range(606):
    if df2['Salary Frequency'][i] == 'Hourly':
        df2['Salary'][i] =  df2['Salary'][i]*2088
    elif df2['Salary Frequency'][i] == 'Daily':
        df2['Salary'][i] =  df2['Salary'][i]*261

contains_ny = df2['Work Location'].str.contains('N.Y.|NYC|Ny|New York|N Y|NY')
address_with_ny = pd.DataFrame(df2['Work Location'][contains_ny])
address_without_ny = df2['Work Location'][~contains_ny]
salary_without_ny = df2['Salary'][~contains_ny]
salary_with_ny = df2['Salary'][contains_ny]
index = pd.Series(address_without_ny.index.values)
address_without_ny = pd.DataFrame([ '% s New York' % i for i in address_without_ny])
address_without_ny = address_without_ny.set_index(index)
address_without_ny = address_without_ny.rename(columns={0:'Work Location'})



'''
the address of with suffix.
'''
a = np.array(address_with_ny)
b=a.tolist()
l1=[]
l2=[]
for c in b:
    '''
    the address could not be identified by geopy
    '''
    if c == ['421 East 26th Street NY NY']:
        lng, lat = -73.9750811, 40.7390769
    elif c == ['2 Lafayette St., N.Y.']:
        lng, lat = -74.0036284, 40.7140838
    elif c == ['4 Metrotech, Brooklyn Ny Ny']:
        lng, lat = -73.985332, 40.694279
    elif c == ['280 Broadway, 7th Floor, N.Y.']:
        lng, lat = -73.985332, 40.694279
    else: 
        lng, lat = geocodeN(c)
    l1.append(lng)
    l2.append(lat)

'''
the address of without suffix.
'''
c = np.array(address_without_ny)
d = a.tolist()
l3=[]
l4=[]
for c in b:
    '''
    the address could not be identified by geopy
    '''
    if c == ['2 Metro Tech New York']:
        lng, lat = -73.9857174, 40.69335
    elif c == ['96-05 Horace Harding Expway New York']:
        lng, lat = -73.8635554, 40.7349322 
    elif c == ['130 Stuyvesant Place, S.I. New York']:
        lng, lat = -74.0770569, 40.6427307 
    elif c == ['Analysis & Reporting New York']:
        continue
    elif c == ['30-30 Thomson Ave L I City Qns New York']:
        lng, lat = -73.9392201,40.7455819    
    elif c == ['28-11 Queens Plaza No., L.I.C. New York']:
        lng, lat = -73.9380597,40.7501382
    elif c == ['11 Metrotech Center New York']:
        lng, lat = -73.985245,40.694303
    elif c == ['34-02 Queens Boulevard Long Is New York']:
        lng, lat = -73.9371935,40.7489932
    else:
        lng, lat = geocodeN(c)
    l3.append(lng)
    l4.append(lat)
    

# In[ ]:


''' reform salary, location in the same dataframe'''

address_without_ny['Salary'] = salary_without_ny
address_with_ny['Salary'] = salary_with_ny
address_without_ny.drop(index=[89,90],inplace=True) 
address_with_ny['Longitude'] = l1
address_without_ny['Longitude'] = l3
address_with_ny['Latitude'] = l2
address_without_ny['Latitude'] = l4
address_without_ny = address_without_ny.reset_index(drop= True)
heatdata = pd.concat([address_without_ny, address_with_ny])
heatdata = heatdata.reset_index(drop= True)


# In[ ]:


'''heatmap'''


import folium
import webbrowser
from folium.plugins import HeatMap

data1 = [[heatdata['Latitude'][i],heatdata['Longitude'][i],heatdata['Salary'][i]/205480] for i in range(604)]
map_osm = folium.Map(location=[40.7,-74],zoom_start=12)    #original map
HeatMap(data1, gradient={.6:'blue', .8:'yellow',1:'red'},name = 'low,wyeufgqwufgiufyqriufgy').add_to(map_osm)  # add heatmap

file_path = r"C:\ucsd\ECE143\salary.html"
map_osm.save(file_path)     # save as html

webbrowser.open(file_path) 

