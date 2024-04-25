# Import the dependencies.
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

# reflect an existing database into a new model
engine = create_engine("sqlite:////Users/jacktemme/Desktop/Data_Challenges/sqlalchemy-challenge/Resources/hawaii.sqlite")
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





#################################################
# Flask Routes
#################################################


