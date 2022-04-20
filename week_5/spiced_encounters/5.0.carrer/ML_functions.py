# import the libraries
import numpy as np

import seaborn as sns # import seaborn for visualization of data
%matplotlib inline
import matplotlib.pyplot as plt#
from datetime import datetime

# read teh two csv files given. Take care of the separator.
df = pd.read_csv('data_train.csv',sep = ',')
df_weather = pd.read_csv('weather.csv',sep = ',')
# Check the shape of the data
df.shape, df_weather.shape
# Now i clean the rows from NaN
result.dropna(how = 'any', inplace = True)
for i in result.columns:
    print(f'Feature {i} has these unique values {result[i].unique()}.')

def import_data():
    import pandas as pd
    df = pd.read_csv('data_train.csv',sep = ',')
