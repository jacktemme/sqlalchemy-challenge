# Import the dependencies.

import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from datetime import datetime as dt

#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
engine = create_engine("sqlite:////Users/jacktemme/Desktop/Data_Challenges/sqlalchemy-challenge/Resources/hawaii.sqlite", echo = False)
# reflect the tables
Base = automap_base()
Base.prepare(autoload_with = engine)

# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(bind = engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)



#################################################
# Flask Routes
#################################################


@app.route("/")
def welcome():
    return (
        "Welcome to an API on Hawaii Weather Data <br/><br/>"
        "The available routes are: <br/>"
        "/api/v1.0/precipitation <br/>"
        "/api/v1.0/stations <br/>"
        "/api/v1.0/tobs <br/>"
        "/api/v1.0/start (input start date as YYYY-MM-DD) <br/>"
        "/api/v1.0/start/end (input start and end date AS YYYY-MM-DD ) <br/>"
        "The oldest date of this database is: 2010-01-01 <br/>"
        "The newest date of this database is: 2017-08-23 "
 )

# Route for date and precipitation in the last year of data

@app.route("/api/v1.0/precipitation")
def precipitation():

    prec_data = session.query(measurement.date, measurement.prcp).filter(measurement.date >= "2016-08-23").all()
    prec_dict = {}
    for row in prec_data:
        prec_dict[row.date] = row.prcp

    return jsonify(prec_dict)


# Route for list of stations
@app.route("/api/v1.0/stations")
def stations():

    station_list = [s.station for s in (session.query(station.station).all())]
    return jsonify(station_list)

# Route for temperature data from the most active station 'USC00519281' in the previous year
@app.route("/api/v1.0/tobs")
def tobs():

    active_station_temp = session.query(measurement.tobs, measurement.date)\
                        .filter(measurement.station == 'USC00519281')\
                        .filter(measurement.date >= "2016-08-23").all()
    tobs_dict ={}
    for row in active_station_temp:
        tobs_dict[row.date] = row.tobs
    return jsonify(tobs_dict)

# Route for min, max and average temperature for specified start range to end of dataset
@app.route("/api/v1.0/<start>")
def start(start):
    try:

        # Check if start and end dates are in correct format (YYYY-MM-DD)
        dt.strptime(start, '%Y-%m-%d')
 
        sel = [func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)]
        start_values = session.query(*sel).filter(measurement.date >= start).all()

        # Put into a dictionary for added readability
        start_dict = {"min": start_values[0][0], 
                    "max" : start_values[0][1],
                    "average": start_values[0][2]}
        
        return jsonify(start_dict)
    
    except ValueError:
         return jsonify({"error": "Character not found. Make sure its formatted YYYY-MM-DD"}), 404

# Route for min, max and average temperature for specified start range to specified end range
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):

    try:

        # Check if start and end dates are in correct format (YYYY-MM-DD)
        dt.strptime(start, '%Y-%m-%d')
        dt.strptime(end, '%Y-%m-%d')
    
        sel = [func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)]
        start_end_values = session.query(*sel).filter(measurement.date >= start)\
                        .filter(measurement.date <= end).all()

        # Put into a dictionary for added readability
        start_end_dict = {"min": start_end_values[0][0], 
                    "max" : start_end_values[0][1],
                    "average": start_end_values[0][2]}
        
        return jsonify(start_end_dict)
    
    except ValueError:
        return jsonify({"error": "Character not found. Make sure its formatted YYYY-MM-DD"}), 404
  
if __name__ == "__main__":
    app.run()

session.close()