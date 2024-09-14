import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import itertools
import gc
import os
import sys
%matplotlib inline

def reduce_memory_usage(df):
    """
    Iterates through all the columns of a DataFrame and modifies the data type
    to reduce memory usage.
    """
    start_mem = df.memory_usage().sum() / 1024**2  # Calculate starting memory usage in MB
    print(f"Memory usage of dataframe is {start_mem:.2f} MB")

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:  # Exclude object (string) types
            c_min = df[col].min()
            c_max = df[col].max()

            # Handle integer types
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)

            # Handle float types
            else:
                if c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)

    end_mem = df.memory_usage().sum() / 1024**2
    print(f"Memory usage after optimization is {end_mem:.2f} MB")
    print(f"Decreased by {(100 * (start_mem - end_mem) / start_mem):.1f}%")

    return df


cab_data=pd.read_csv('test_cab_fare.csv')
cab_data=reduce_memory_usage(cab_data)
weath_data=pd.read_csv('Weather Data.csv')
weath_data=reduce_memory_usage(weath_data)

cab_data.head()

weath_data.head()

weath_data.columns

import datetime
cab_data['datetime']=pd.to_datetime(cab_data['pickup_datetime'])
weath_data['datetime']=pd.to_datetime(weath_data['Date/Time'])


cab_data.head()

cab_data.shape

weath_data.shape

cab_data.describe()
cab_data.isnull().sum()

weath_data.describe()
weath_data.isnull().sum()

a=pd.concat([cab_data,weath_data])

a.replace(0,np.nan,inplace=True)
numeric_cols = a.select_dtypes(include='number')
a[numeric_cols.columns]=numeric_cols.fillna(numeric_cols.median())


a.tail()

a.drop(['Weather'],axis=1,inplace=True)

a.head()

a.groupby('passenger_count').count().plot.bar()

a['passenger_count'].value_counts().plot(kind='bar',figsize=(10,5),color='pink')

import matplotlib.pyplot as plt
x=a['pickup_longitude']
y=a['pickup_latitude']
plt.plot(x,y)
plt.show()

a.to_csv('new.csv',index=False)

a.drop('Date/Time',inplace=True,axis=1)

a.head()

a = a.rename(columns={'datetime': 'dropoff_datetime'})
a['pickup_datetime'] = pd.to_datetime(a['pickup_datetime'].dt.tz_localize(None))
a['dropoff_datetime'] = pd.to_datetime(a['dropoff_datetime'].dt.tz_localize(None))



a['duration']=(a['dropoff_datetime']-a['pickup_datetime']).dt.total_secons

a['duration'].value_counts()

