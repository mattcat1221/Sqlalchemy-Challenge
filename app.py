# Import the dependencies.
import sqlalchemy
import datetime as dt
from flask import Flask, jsonify
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base

#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
M = Base.classes.measurement
S = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return ('''
            <h1> Hawaii's Climate Analysis API</h1>
            
            <h3>The following links are available:</h3>
            
            <ul>
                <li><a href="/api/v1.0/stations">Stations</a></li>
                <li><a href="/api/v1.0/precipitation">Precipitation</a></li>
                <li><a href="/api/v1.0/tobs">temperature Observed</a></li>
                <li><a href="/api/v1.0/2016-08-23">Change start date for different result</a></li>
                <li><a href="/api/v1.0/2016-08-23/2017-08-23">Change start and end date for different result</a></li>
            </ul>
''')
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(M.date, M.prcp).filter(M.date>='2016-08-023').all()
    return { date:prcp for date,prcp in results}

@app.route("/api/v1.0/stations")
def station():
    
    return { id:loc for id,loc in session.query(S.station, S.name).all()}

@app.route("/api/v1.0/tobs")
def tobs():
    
    results = session.query(
        M.date,
        M.tobs
    ).filter(
        (M.date>='2016-08-023') &
        (M.station=='USC00519281')
    ).all()
    
    return { date:prcp for date,prcp in results}

@app.route('/api/v1.0/<start>', methods=['GET'])
@app.route('/api/v1.0/<start>/<end>', methods=['GET'])
def temperature_stats(start, end=None):
    #Return the minimum, average, and maximum temperatures for a given start date or a range from start date to end date.
    if end:
        results = session.query(
            func.min(M.tobs),
            func.avg(M.tobs),
            func.max(M.tobs)
        ).filter(M.date >= start).filter(M.date <= end).all()
    else:
        results = session.query(
            func.min(M.tobs),
            func.avg(M.tobs),
            func.max(M.tobs)
        ).filter(M.date >= start).all()

    # Extract the results
    temps = list(results[0])
    temp_data = {
        "TMIN": temps[0],
        "TAVG": temps[1],
        "TMAX": temps[2]
    }
    # Return results as a JSON response
    return jsonify(temp_data)
    
# Close Session
session.close()

if __name__ == "__main__":
    app.run(debug=True)