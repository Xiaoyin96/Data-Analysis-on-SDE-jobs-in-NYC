
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


# ### Data Preprocessing

# In[10]:


# Read the original csv file
df = pd.read_csv('NYC_Jobs.csv')
# Delete irrelevant columns
df1 = df.drop(columns = ['Job ID','Posting Date','Posting Updated','Process Date','Agency','Level','Civil Service Title','To Apply','Title Code No'])
df1.head()


# In[11]:


# Count Job Category
pd.DataFrame(df1['Job Category'].value_counts()).head()



# In[12]:


# Uppercase all the words in data in order to search keyword
df2 = df1.apply(lambda x: x.astype(str).str.upper())
# Sort software related jobs using keyword Data and Technology in job categories
df3 = df2[df2['Job Category'].str.contains('DATA|TECHNOLOGY').replace(np.nan, False, regex=True)]
pd.DataFrame(df3['Job Category'].value_counts())


# In[13]:


# Then search software related keywords in business title
df4 = df3[df3['Business Title'].str.contains('INFORMATION|SOFTWARE|DATA|NETWORK|ANALYST|IT|DEVELOPER').replace(np.nan, False, regex=True)]
df4.head()


# Until now, we have the processed data, containing 373 software related jobs and their detailed information.
