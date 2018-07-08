
Step 1 - Data Engineering

The climate data for Hawaii is provided through two CSV files. Start by using Python and Pandas to inspect the content of these files and clean the data.


Create a Jupyter Notebook file called data_engineering.ipynb and use this to complete all of your Data Engineering tasks.
Use Pandas to read in the measurement and station CSV files as DataFrames.
Inspect the data for NaNs and missing values. You must decide what to do with this data.
Save your cleaned CSV files with the prefix clean_.


```python
import pandas as pd
```


```python
#Use Pandas to read in the measurement and station CSV files as DataFrames.
station_df = pd.read_csv("Resources/hawaii_stations.csv")
measure_df = pd.read_csv("Resources/hawaii_measurements.csv")
```


```python
station_df
```


```python
measure_df
```


```python
measure_df.isnull().any()
```


```python
#Inspect the data for NaNs and missing values. You must decide what to do with this data.
measure_df = measure_df.fillna(0)
```


```python
#Save your cleaned CSV files with the prefix clean_.
measure_df.to_csv("Resources/clean_hawaii_measurements.csv", index=False)
```
