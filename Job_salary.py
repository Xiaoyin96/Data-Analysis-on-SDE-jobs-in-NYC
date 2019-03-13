'''
To deal with the relation between job categories and salary.
'''
#Import
import pandas as pd
import numpy as np
import string
import matplotlib.pyplot as plt
import altair as alt
from altair import Chart, load_dataset

#Data selection
data_v1 = pd.read_csv('data_v1.csv')
df=data_v1.loc[:,['Job Category','Salary Range From']]
df=df.dropna()

#Filtering out hour salary and restore the annual salary
df=df[df['Salary Range From']>1000]
data=[]

#Reserve the first word in 'Job Description'
for i in df['Job Category']:
    z=i
    for m in i:
        if m in string.punctuation+',':
            i=i.replace(m,'')
            z=i.replace(m,'')
    data.append(z)
df1=pd.DataFrame(data)
data1=[]
data=[]
data2=[]
for i in df1.loc[:,0]:
    data1.append(i.split(' ' or ','))
for i in df.loc[:,'Salary Range From']:
    data2.append(i)
for index in range(len(data1)):
    data.append(data1[index][0])
df2=pd.DataFrame(data)
df2.rename(columns={df2.columns[0]:'Job'},inplace=True)

#Sum up the number of positions in 'Other' category
index=0
for i in df2.loc[:,'Job']:
    if i=='Policy' or i=='Communications' or i=='Social' or i=='Information' or i=='Clerical' or i=='Maintenance' or i=='Community':
        df2.loc[index]='Others'
    index+=1
numb_job=pd.value_counts(df2['Job'])

#Reserve the respective salary according to 'Job Description' 
df3=pd.DataFrame(data2)
df3.rename(columns={df3.columns[0]:'Salary Range From'},inplace=True)
data_update=pd.concat([df2,df3],axis=1)
summation=np.zeros([1,len(numb_job)])
salary=np.zeros(len(numb_job))
for i in range(len(df2)):
    for j in range(len(numb_job)):
        if data_update.loc[i,'Job']==numb_job.index[j]:
            summation[0,j]=summation[0,j]+data_update.loc[i,'Salary Range From']
for i in range(len(numb_job)):
    summation[0,i]=summation[0,i]/numb_job[i]

#Create a dataframe with updated 'Job Description' and 'Salary' 
df4=pd.DataFrame(numb_job.index)
df4.rename(columns={df4.columns[0]:'Job'},inplace=True)
df5=pd.DataFrame(np.transpose(summation))
df5.rename(columns={df5.columns[0]:'average'},inplace=True)
data_average=pd.concat([df4,df5],axis=1)
chart2=Chart(data_average)
chart2.mark_point().encode(x='average',y='Job',color='Job')
#plt.scatter(data_update['Salary Range From'],data_update['Job'])
#plt.show()





#Altair plot
chart=Chart(data_update)
chart.mark_point().encode(x='Salary Range From',y='Job',color='Job')



