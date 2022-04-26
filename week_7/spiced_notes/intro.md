# WEEK 07: INTRODUCTION TO TIME SERIES
- Back to machine learning as we did in week 2 - week 4

## Time series modeling: 
- What examples of time series data can you think of?
    - weather data: e.g. air quality data, precipitation, wind, temperature, humidity, vorticity, divergence
    - Economic data: GDP, unemployment rate
    - Stock market
    - Housing prices
    - public transport


## Modeling of time series.
**Decomposition of a time series**
Decomposing  a time series (we are going to do this today) into its compones:
    - Trend
    - Seasonality
    - Remainder:
        - This is the part that is extremely intereseting for us. It is what we model. To get the remainder, we decompose the timeseries by removing the trend and the seasonality. The remainder is said to be stationary in time.
    
# PROJECT FOR THE WEEK

## GOAL:
- The goal this week is to build a model that is able to make short term temperature forecasts e.g. mean temperature for tomorrow given timeseries data upto today.

## DATA:
- For the project:
    - Use mean daily temperature data for a station of your choice
    - follow the instructions in the course material to download data from ECDA for Berlin-Tempelhof.

- For the encounters:
    - we are going to use the flights data set in seaborn (no. of airline passengers between 1949 and 1960)

### YOUR TASKS:
- Download the data
- Perform EDA (Exploratory Data Analysis)
    - clean the data
    - plot the data