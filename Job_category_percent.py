"""
To calculate the job category distribution.
A pie fig is provided.
"""
#import
import pandas as pd
import numpy as np
import string
import matplotlib.pyplot as plt

#Preprocessing to drop 'nan' values
data_v1 = pd.read_csv('data_v1.csv')
df=data_v1.loc[:,'Job Category']
df=df.dropna()

#String split and storage; reserve the first word as the job description
data=[]
for i in df:
    z=i
    for m in i:
        if m in string.punctuation+',':
            i=i.replace(m,'')
            z=i.replace(m,'')
    data.append(z)
df1=pd.DataFrame(data)
data1=[]
data=[]
for i in df1.loc[:,0]:
    data1.append(i.split(' ' or ','))
for index in range(len(data1)):
    data.append(data1[index][0])
data_new=pd.Series(data)
a=pd.value_counts(data_new)

#sum up the category with small numbers as Category: 'Other'
labels=list(a.index)
value=list(a)
labels[9]='Others'
labels=np.delete(labels,[10,11,12,13,14,15],axis=0)
value[9]=sum(value[9:16])
value=np.delete(value,[10,11,12,13,14,15],axis=0)

#fig plot
explode=(0.1,0,0,0,0,0,0,0,0,0)
plt.pie(value,autopct='%.1f%%',labels=labels,explode=explode,
        shadow=True,startangle=90)
plt.title('Top 10 Job Category')
plt.show()

