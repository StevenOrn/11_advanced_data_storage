import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.Station
Measurement = Base.classes.Measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"

    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of precipitation"""

    results = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>'2016-08-23').order_by(Measurement.date).all()

    precip_data= []

    for result in results:
        precip_dict ={result[0]:result[1]}
        precip_data.append(precip_dict)

    return jsonify(precip_data)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""

        # Query all stations
    results = session.query(Station.station).all()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of temperature observations"""

    results = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date>'2016-08-23').order_by(Measurement.date).all()

    temp_data= []

    for result in results:
        temp_dict ={result[0]:result[1]}
        temp_data.append(temp_dict)

    return jsonify(temp_data)


@app.route("/api/v1.0/temp/<start_date>")
def temp_start(start_date):
    """Return a min_temp, avg_temp, max_temp for a date range"""


    results = session.query(Measurement.tobs).filter(Measurement.date>start_date).order_by(Measurement.tobs.desc()).all()
    
    min_temp = results[-1][0]
    avg_temp = np.mean(results)
    max_temp = results[0][0]
    
    return jsonify(min_temp,avg_temp,max_temp)


@app.route("/api/v1.0/temp/<start_date>/<end_date>")
def calc_temps(start_date,end_date):
    """Return a min_temp, avg_temp, max_temp for a date range"""


    results = session.query(Measurement.tobs).filter(Measurement.date<end_date).filter(Measurement.date>start_date).order_by(Measurement.tobs.desc()).all()
    
    min_temp = results[-1][0]
    avg_temp = np.mean(results)
    max_temp = results[0][0]
    
    return jsonify(min_temp,avg_temp,max_temp)






if __name__ == '__main__':
    app.run(debug=True)
