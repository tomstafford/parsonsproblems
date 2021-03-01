df.columns=['yyyy','mm','temp_max','temp_min','airfrost','rain','sun'] #rename the columns to be a bit more readable

import matplotlib.pyplot as plt #plotting functions
vars_to_convert=["temp_max", "temp_min","airfrost","sun"] #list of variables to change to numeric type
import os #file and folder functions
import numpy as np #number functions
df.groupby('mm')['temp_max'].mean().plot(label='max',color='r') #plot average max temp for each month
plt.xlabel('Month (1-12)') #xlabels
plt.savefig(os.path.join('outputs','minmaxtemp.png')) #export
plt.legend(loc=0) #add legend

print(df.dtypes) #check what data types the columns imported as 

df.to_csv(os.path.join('outputs','shefmetdat.csv')) #export prcoessed data to csv
print(df.dtypes) #check what data types the columns are now



df[vars_to_convert] = df[vars_to_convert].apply(pd.to_numeric) #convert some variables to numeric type




"""MET office data for the sheffield station from https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/sheffielddata.txt"""

plt.clf() #clean existing plot, if any
plt.ylabel('Average max/min tempreture in degree C') #ylabels
df.groupby('mm')['temp_min'].mean().plot(label='min',color='b') #plot average max temp for each month
df=pd.read_csv(os.path.join('inputs','sheffieldmetdata_cleaned.txt'),skiprows=[1],sep='\s{1,}') #import data, using 1 or more space as the seperator
df.replace('---',np.nan,inplace=True) #replace all the ---s with NaNs to indicate missing data
import pandas as pd #dataframes
