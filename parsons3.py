
plt.ylabel('Average max/min tempreture in degree C') #ylabels
df=pd.read_csv(os.path.join('inputs','sheffieldmetdata_cleaned.txt'),skiprows=[1],sep='\s{1,}') #import data, using 1 or more space as the seperator
df.groupby('mm')['temp_max'].mean().plot(label='max',color='r') #plot average max temp for each month


df.groupby('mm')['temp_min'].mean().plot(label='min',color='b') #plot average max temp for each month

"""MET office data for the sheffield station from https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/sheffielddata.txt"""

df[vars_to_convert] = df[vars_to_convert].apply(pd.to_numeric) #convert some variables to numeric type
print(df.dtypes) #check what data types the columns are now
plt.clf() #clean existing plot, if any


plt.legend(loc=0) #add legend
df.replace('---',np.nan,inplace=True) #replace all the ---s with NaNs to indicate missing data
df.columns=['yyyy','mm','temp_max','temp_min','airfrost','rain','sun'] #rename the columns to be a bit more readable

import os #file and folder functions
plt.savefig(os.path.join('outputs','minmaxtemp.png')) #export
vars_to_convert=["temp_max", "temp_min","airfrost","sun"] #list of variables to change to numeric type
df.to_csv(os.path.join('outputs','shefmetdat.csv')) #export prcoessed data to csv
import numpy as np #number functions
import matplotlib.pyplot as plt #plotting functions
print(df.dtypes) #check what data types the columns imported as 

plt.xlabel('Month (1-12)') #xlabels

import pandas as pd #dataframes

