# Autoregressive model

21/04/2022

### Time Series

Measurements over time with different properties:
	**Trends**: Persistent longterm change, slowest moving part
	**Seasons**: Regular, calendar-based periodic changes
	**Cycles**: Not calendar-based periodic changes 

### Stationarity

Time series main characteristics are not changing over time, are not time dependent.  
Difference to white noise, it's not completely random and the mean is not zero

To make a time series stationary:   
	1 - Differencing the Series (once or more)   
	2 - Take the log of the series   
	3 - Take the nth root of the series    
	4 - Combination of the above

### Autocorrelation

Stationarity can be investigated by ACF (Autocorrelation function)   
Several measures can be used to test for stationarity as well:
	1 - Augmented Dickey Fuller test (ADH Test)   
	2 - Kwiatkowski-Phillips-Schmidt-Shin – KPSS test (trend stationary)   
	3 - Philips Perron test (PP Test)   

Rules of thumb:       

- If the ACF plot declines gradually and the PACF drops instantly, use Auto Regressive model.
- If the ACF plot drops instantly and the PACF declines gradually, use Moving Average model.
- If both ACF and PACF decline gradually, combine Auto Regressive and Moving Average models (ARMA).
- If both ACF and PACF drop instantly (no significant lags), it’s likely you won’t be able to model the time series.

Autocorrelation is the correlation between the time series and a lag series     
Partial autocorrelation is the pure correlation of a lag, excluding correlations from intermediate lags 

```{python}
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
```

### Further reading

* [Complete time series analysis](https://www.machinelearningplus.com/time-series/time-series-analysis-python/)
* [Autocorrelation and partial autocorrelation](https://statisticsbyjim.com/time-series/autocorrelation-partial-autocorrelation/)

