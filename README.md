## ECE143 Project 
### Data Analysis on Software Engineering Related Jobs in New York City
----
This is a repository for ECE143 course in UCSD.  
Team members: Kuan-Wei Chen, Xiaoyin Yang, Houjian Yu and Yu Shi.

### Environment and requirement
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
```
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
```
```


#### Part 1 Data Processing
We use the dataset [NYC_jobs](https://catalog.data.gov/dataset/nyc-jobs-26c80) from the government website.
