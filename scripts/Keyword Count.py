
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)


# ### Keyword count in software related jobs

# In[14]:


def split_count(x,s):
    '''
    This is a function aiming to split each string in a column and output a keyword count dataframe
    Input:
    x: should be a dataframe
    s: string of column name
    
    Output: pd.series
    '''
    assert isinstance(x,pd.core.frame.DataFrame)
    a=x[s].str.split(',|;| ', expand=True).stack().reset_index(level=1,drop=True).reset_index(drop=True).map(str.strip).value_counts()
    return a


# ### Count the requirement keyword

# In[15]:


req = pd.DataFrame(split_count(df4,'Minimum Qual Requirements')) 
# req1 focuses on degree.
req1 = pd.DataFrame(req, index=['PH.D.','MASTER','BACCALAUREATE','COLLEGE'])
req1.rename(columns={0:'Count'}, inplace=True)
data0 = [go.Bar(
            x=req1.index,
            y=req1['Count']
    )]

iplot(data0, filename='general skill')

# req2 focuses on ability.
req2 = pd.DataFrame(req, index=['COMPUTER','PROFESSIONAL','DATA','EXPERIENCE','PROGRAMMING','SOFTWARE','SCIENCE'])
req2.rename(columns={0:'Count'}, inplace=True)
req2.plot.bar()
plt.title('Capability requirements keyword count')
plt.show()



# ### Count the skill related keyword

# In[16]:


# Count general skills keyword
skill = pd.DataFrame(split_count(df4,'Preferred Skills'))
skill_1 = pd.DataFrame(skill,index=['EXPERIENCE','MANAGEMENT','DATA','COMMUNICATION','BUSINESS','SOFTWARE','NETWORK','TEAM','VERBAL','DESIGN','ENTERPRISE','ARCHITECTURE','ANALYSIS'])
skill_1.rename(columns={0:'Count'}, inplace=True)
data1 = [go.Bar(
            x=skill_1.index,
            y=skill_1['Count']
    )]

py.iplot(data1, filename='general skill')

# Count programming language skills keyword
skill_2 = pd.DataFrame(skill,index=['SQL','MICROSOFT','DATABASE','JAVA','.NET','C#','ORACLE','CISCO','JAVASCRIPT','HTML','PYTHON'])
skill_2.rename(columns={0:'Count'}, inplace=True)
data2 = [go.Bar(
            x=skill_2.index,
            y=skill_2['Count']
    )]

py.iplot(data2, filename='basic-bar')


# ### Count keyword in business title in software related jobs

# In[17]:


title = pd.DataFrame(split_count(df4,'Business Title'))
title1 = pd.DataFrame(title,index=['ANALYST','DEVELOPER','MANAGER','ENGINEER','ADMINISTRATOR','SPECIALIST','CHIEF','OFFICER','DIRECTOR','SUPERVISOR','TECHNICIAN'])
title1.rename(columns={0:'Count'},inplace=True)
labels = title1.index
values = title1['Count']
trace = go.Pie(labels=labels, values=values)
py.iplot([trace])

