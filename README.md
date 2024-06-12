# Sqlalchemy-Challenge

![MIT](https://img.shields.io/badge/License-MIT-blue)

## Website: 
[website](https://github.com/mattcat1221/Sqlalchemy-Challenge/blob/main/README.md)

## Description
Step 1 - Analyzed precipitation data in Hawaii.

So I decided to treat myself to a long vacation in Honolulu, Hawaii! When planning a trip, I need to do a climate analysis of the area. The following describes what I need to do.Step 1 - Climate Analysis and ResearchFirst, I did a basic climate analysis using Python and SQLAlchemy and examined data from the climate database I found.Select the start and end date of the trip. The vacation time is about 3-15 days in total.I used SQLAlchemy's create_engine to connect to the sqlite database.Used SQLAlchemy's automap_base() function to map tables to classes and store a reference to classes called Station and Measurement.Precipitation analysisSuggested query to retrieve last 12 months of precipitation data.Only date and prcp values ​​are selected.Loaded the search results into a Panda DataFrame and set the index on the date column.DataFrame values ​​sorted by date.Graph the results using the DataFrame's graph method..
Analyzes precipitation data in Hawaii 


Step 2 - Climate App

After completing my initial analysis, I designed a Flask API based on the queries that I have just developed.

Used FLASK to create my routes.
Routes

/

/api/v1.0/precipitation

/api/v1.0/stations

/api/v1.0/tobs

/api/v1.0/<start>

/api/v1.0/<start>/<end>

https://share.icloud.com/photos/097BvJ6_fc5qHoHBdkqA5Z_yA
https://github.com/mattcat1221/Sqlalchemy-Challenge/assets/158774626/9df647bb-a437-454d-b161-75e438e4fd09)



<img width="625" alt="Screenshot 2024-06-10 at 2 23 31 PM" src="https://github.com/mattcat1221/Sqlalchemy-Challenge/assets/158774626/d90b086e-bdf6-4361-a1ad-e5ef50df4d6e">
https://github.com/mattcat1221/Sqlalchemy-Challenge/assets/158774626/9b361986-1963-4309-bdba-2a991eb4716e



## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)
- [Features](#features)

- [Contact](#contact)

## Installation
jupyterlab
python
sqlalchemy 
Matplotlib 
Pandas

## Usage
educational

## Credits
Catherine Matthews 

## License
MIT

## Features
datatables and graphs 



## Contact
If there are any questions of concerns, I can be reached at:
##### [github: matcat1221](https://github.com/matcat1221)
##### [email: caseyvmatthews@gmail.com](mailto:caseyvmatthews@gmail.com)
