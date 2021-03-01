"""Now let's talk about climate change"""

import pandas as pd #dataframes
import numpy as np #number functions
import matplotlib.pyplot as plt #plotting functions
import os #file and folder functions

df=pd.read_csv(os.path.join('outputs','shefmetdat.csv')) #import cleaned data we exported from the previous script parsons3.py

print(df.dtypes) #check what data types the columns imported as 

max_temp_mean=df.groupby('mm')['temp_max'].mean() #average max temp for each month
max_temp_stdv=df.groupby('mm')['temp_max'].std() #stdev of max temp for each month

def zscorefunc(df,meanval,stdval): #function to calculate z scores
    return (df['temp_max']-meanval[df['mm']])/stdval[df['mm']] #return z score = val-mean/stv

args=(max_temp_mean,max_temp_stdv) #arguments we will pass to the function
df['ztempmax']=df.apply(zscorefunc,args=args,axis=1) #create new colum with z score of temp for each month

plt.clf() #clear any existing plots
df.groupby('mm')['ztempmax'].mean().plot() #sanity check - average z score should be close to zero

df2=df.groupby('yyyy')['ztempmax'].mean().reset_index()  # find average z score for each year
df2['5year_average']=df2['ztempmax'].rolling(center=False,window=5).mean() #create 5 year rolling average 

plt.clf() #clear any existing plots
plt.plot(df2['yyyy'],df2['ztempmax'],'.',color='b',ms=5,label='yearly average') #scatter plot of yearly averages
plt.plot(df2['yyyy'],df2['5year_average'],color='r',lw=3,label='5 year rolling mean') #line of rolling average
plt.ylabel('Average z score of max monthly temperature') #add y label
plt.xlabel('year') #add x label
plt.legend(loc=0) #add legend
plt.savefig(os.path.join('outputs','sheffield1883-2019.png')) #save figure
#conclusion = be terrified of climate change?
