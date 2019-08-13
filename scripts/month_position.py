#import
import pandas as pd
import plotly.plotly as py
import numpy as np
from bokeh.plotting import figure, output_file, show

#preprocessing
def split_count(x,s):
    assert isinstance(x,pd.core.frame.DataFrame)
    a=x[s].str.split(',|;| ', expand=True).stack().reset_index(level=1,drop=True).reset_index(drop=True).map(str.strip).value_counts()
    return a
df = pd.read_csv('NYC_Jobs.csv')
df1 = df.drop(columns = ['Job ID','Posting Updated','Post Until','Process Date','Agency','Level','Civil Service Title','To Apply','Title Code No'])
df1.head() # version 1 deletes some useless columns
pd.DataFrame(df1['Job Category'].value_counts())
df2 = df1.apply(lambda x: x.astype(str).str.upper())

#filter out part-time
mon_df2=df2[df2['Salary Range From']>'1000']
#classify the data according to keywords
mon_df=pd.DataFrame(df2['Posting Date'])
month=['-01-','-02-','-03-','-04-','-05-','-06-','-07-','-08-','-09-','-10-','-11-','-12-']
job_numb_permonth=np.zeros((12,1))
#month_m=np.array([['Jan.','Feb.','Mar.','Apr.','May.','June.','July.','Aug.','Sept.','Oct.','Nov.','Dec.']]).T
month_m=np.array([[1,2,3,4,5,6,7,8,9,10,11,12]]).T

#count
for i in range(len(mon_df)):
    for j in range(len(month)):
        if month[j] in mon_df.loc[i,'Posting Date']:
            job_numb_permonth[j,0]=job_numb_permonth[j,0]+1
#month_m=pd.DataFrame(month_m)
#job_numb_permonth=pd.DataFrame(job_numb_permonth)

#figure
p = figure(title="Positions per month", # title of figure
           x_axis_label='Months', 
           y_axis_label='Number of positions',
           width= 400,  # figure width
           height = 300) # figure height
p.line(month_m[:,0], job_numb_permonth[:,0], legend=None, line_width=2)  # width of line
p.circle(month_m[:,0],job_numb_permonth[:,0],radius=0.2,fill_color='red')
show(p)

            
