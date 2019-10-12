# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../../var/folders/_7/1vq2g6rn6y37kmg6k2lpq33m0000gn/T'))
	print(os.getcwd())
except:
	pass
#%%
from IPython import get_ipython


#%%
def read_auto_data(fileName = 'Automobile_price_data.csv'):
    'Function to load the auto price data set from a .csv file'
    import pandas as pd
    import numpy as np

    ## Read csv file
    dataframe = pd.read_csv(fileName)

    ## Remove rows with missing values
    columns = ['price', 'bore', 'stroke', 'horsepower', 'peak-rpm']
    for column in columns:
        dataframe.loc[dataframe[column] == '?', column] = np.nan
    dataframe.dropna(axis=0, inplace = True)

    ## Convert columns to numeric values
    for column in columns:
        dataframe[column] = pd.to_numeric(dataframe[column])
    return dataframe

dataframe = read_auto_data()


#%%
dataframe.head()


#%%
dataframe.describe()


#%%
import matplotlib.pyplot as pyplot
get_ipython().magic(u'matplotlib inline')
pyplot.plot(dataframe['city-mpg'], dataframe['price'], 'ro')


#%%


