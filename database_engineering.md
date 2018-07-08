
Step 2 - Database Engineering

Use SQLAlchemy to model your table schemas and create a sqlite database for your tables. You will need one table for measurements and one for stations.


Create a Jupyter Notebook called database_engineering.ipynb and use this to complete all of your Database Engineering work.
Use Pandas to read your cleaned measurements and stations CSV data.
Use the engine and connection string to create a database called hawaii.sqlite.

Use declarative_base and create ORM classes for each table.


You will need a class for Measurement and for Station.
Make sure to define your primary keys.


Once you have your ORM classes defined, create the tables in the database using create_all.


```python
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```


```python
#Use Pandas to read your cleaned measurements and stations CSV data.
station_df = pd.read_csv("Resources/hawaii_stations.csv")
measurement_df = pd.read_csv("Resources/clean_hawaii_measurements.csv")
```


```python
station_df#.keys()
```


```python
measurement_df.head()#.keys()
```


```python
class Station(Base):
    __tablename__ = "Station"
    station = Column(String, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
```


```python
class Measurement(Base):
    __tablename__ = "Measurement"
    id = Column(Integer, primary_key=True)
    station = Column(String)
    date = Column(String)
    prcp = Column(Float)
    tobs = Column(Integer)
```


```python
#Use the engine and connection string to create a database called hawaii.sqlite.
engine = create_engine("sqlite:///hawaii.sqlite")
```


```python
Base.metadata.create_all(engine)
```


```python
session = Session(engine)
```


```python
#station_df.to_sql('Station',con=engine, if_exists='replace',index=False)

for i in range(len(station_df)):
    session.add(Station(station = station_df['station'][i], name = station_df['name'][i],
                        latitude = station_df['latitude'][i], longitude = station_df['longitude'][i],
                        elevation = station_df['elevation'][i] ) )
    

```


```python
# measurement_df.to_sql('Measurement',con=engine, if_exists='replace',index=False)

for i in range(len(measurement_df)):
    session.add(Measurement(station = measurement_df['station'][i], date = measurement_df['date'][i], 
                            prcp = measurement_df['prcp'][i], tobs = int(measurement_df['tobs'][i])))

```


```python
session.commit()
```


```python
engine.execute().fetchall()
```


```python
engine.execute('select * from measurement').fetchall()
```
