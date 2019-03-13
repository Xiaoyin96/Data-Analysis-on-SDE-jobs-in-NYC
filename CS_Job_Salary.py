#import
import pandas as pd
import plotly.plotly as py
import numpy as np
import plotly
import plotly.graph_objs as go
import altair as alt
from altair import Chart, load_dataset,X, Y, Axis, SortField, Scale

#preprocessing
def split_count(x,s):
    assert isinstance(x,pd.core.frame.DataFrame)
    a=x[s].str.split(',|;| ', expand=True).stack().reset_index(level=1,drop=True).reset_index(drop=True).map(str.strip).value_counts()
    return a

df = pd.read_csv('NYC_Jobs.csv')
df1 = df.drop(columns = ['Job ID','Posting Date','Posting Updated','Process Date','Agency','Level','Civil Service Title','To Apply','Title Code No'])
df1.head() # version 1 deletes some useless columns
pd.DataFrame(df1['Job Category'].value_counts())
df2 = df1.apply(lambda x: x.astype(str).str.upper())
df3 = df2[df2['Job Category'].str.contains('DATA|TECHNOLOGY').replace(np.nan, False, regex=True)] # sort by keyword in categories
df4 = df3[df3['Business Title'].str.contains('INFORMATION|SOFTWARE|DATA|NETWORK|ANALYST|IT|DEVELOPER').replace(np.nan, False, regex=True)]

#count specific title name in 'Business Title'
data_sf1=[]
data_sf2=[]
for i in df3.index:
    if 'ANALYST' in df3.loc[i,'Business Title'] and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('ANALYST')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'DEVELOPER' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('DEVELOPER')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'MANAGER' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('MANAGER')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'ENGINEER' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('ENGINEER')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'ANALYST' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('ANALYST')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'ADMINISTRATOR' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('ADMINISTRATOR')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'SPECIALIST' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('SPECIALIST')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'CHIEF' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('CHIEF')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'OFFICER' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('OFFICER')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'DIRECTOR' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('DIRECTOR')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'SUPERVISOR' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('SUPERVISOR')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))
    if 'TECHNICIAN' in df3.loc[i,'Business Title']and float(df3.loc[i,'Salary Range From'])>10000:
        data_sf1.append('TECHNICIAN')
        data_sf2.append(float(df3.loc[i,'Salary Range From']))

#calculate respective salary
data_sf1=pd.DataFrame(data_sf1)
data_sf2=pd.DataFrame(data_sf2)
data_sf1.rename(columns={data_sf1.columns[0]:'Job'},inplace=True)
data_sf2.rename(columns={data_sf2.columns[0]:'Salary Range From'},inplace=True)
data_conv=pd.concat([data_sf1,data_sf2],axis=1)
numb_job=pd.value_counts(data_sf1['Job'])
summation=np.zeros([len(numb_job),1])
for i in range(len(numb_job)):
    for j in range(len(data_conv)):
        if data_conv.loc[j,'Job']==numb_job.index[i]:
            summation[i,0]=summation[i,0]+float(data_conv.loc[j,'Salary Range From'])
for i in range(len(summation)):
    summation[i,0]=summation[i,0]/numb_job[i]
df_41=pd.DataFrame(numb_job.index)
df_41.rename(columns={df_41.columns[0]:'Job'},inplace=True)
df_51=pd.DataFrame(summation)
df_51.rename(columns={df_51.columns[0]:'Salary Range From'},inplace=True)
data_average=pd.concat([df_41,df_51],axis=1)

#fig
chart1=Chart(data_average)
h1=chart1.mark_point(size=300,filled=True,color='Red').encode(x='Salary Range From',y='Job')
chart2=Chart(data_conv)
h2=chart2.mark_point().encode(x='Salary Range From',y='Job',color='Job')
h1+h2



