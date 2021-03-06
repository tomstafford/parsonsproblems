plt.xlabel('year') #add x label
max_temp_mean=df.groupby('mm')['temp_max'].mean() #average max temp for each month
plt.clf() #clear any existing plots
plt.plot(df2['yyyy'],df2['5year_average'],color='r',lw=3,label='5 year rolling mean') #line of rolling average
df=pd.read_csv(os.path.join('outputs','shefmetdat.csv')) #import cleaned data we exported from the previous script parsons3.py

import os #file and folder functions
df.groupby('mm')['ztempmax'].mean().plot() #sanity check - average z score should be close to zero

import pandas as pd #dataframes
    return (df['temp_max']-meanval[df['mm']])/stdval[df['mm']] #return z score = val-mean/stv


df2=df.groupby('yyyy')['ztempmax'].mean().reset_index()  # find average z score for each year
args=(max_temp_mean,max_temp_stdv) #arguments we will pass to the function

def zscorefunc(df,meanval,stdval): #function to calculate z scores
plt.clf() #clear any existing plots
max_temp_stdv=df.groupby('mm')['temp_max'].std() #stdev of max temp for each month
plt.ylabel('Average z score of max monthly temperature') #add y label
df['ztempmax']=df.apply(zscorefunc,args=args,axis=1) #create new colum with z score of temp for each month
plt.savefig(os.path.join('outputs','sheffield1883-2019.png')) #save figure

df2['5year_average']=df2['ztempmax'].rolling(center=False,window=5).mean() #create 5 year rolling average 
import numpy as np #number functions
#conclusion = be terrified of climate change?
import matplotlib.pyplot as plt #plotting functions

plt.legend(loc=0) #add legend

print(df.dtypes) #check what data types the columns imported as 
"""Now let's talk about climate change"""
plt.plot(df2['yyyy'],df2['ztempmax'],'.',color='b',ms=5,label='yearly average') #scatter plot of yearly averages

