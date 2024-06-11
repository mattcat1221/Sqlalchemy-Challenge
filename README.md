# Sqlalchemy-Challenge

![MIT](https://img.shields.io/badge/License-MIT-blue)

## Website: 
[website](https://github.com/mattcat1221/Sqlalchemy-Challenge/blob/main/README.md)

## Description
Analyzes precipitation data in Hawaii 


This project uses Python and SQLAlchemy to do basic data exploration and analysis of an SQLite climate database. All analysis is done using SQLAlchemy (ORM queries), Pandas, and Matplotlib. It also provides an API (designed using Flask) for querying this climate data.

Part I: Exploratory Climate Analysis

This part of the project analyzes Hawaii precipitation and weather station data, and produces visualizations of rainfall and temperature patterns. It also supports the planning of visits to Hawaii with:

local precipitation summaries for each of the local weather stations and
temperature dailies for a flexible range of trip dates.
It consists of:

a SQLite database (Resources/Hawaii.sqlite)
a Jupyter notebook (sqlalchemy-challenge/climate_analysis.ipnyb) that uses SQLAlchemy, Python Pandas and MatPlotlib to analyze and visualize this data.
Bar charts, a histogram and an area chart that are visible within the notebook and also stored as .png files in the sqlalchemy-challenge folder.
Part II: Climate App

This part of the project surfaces several SQLAlchemy precipitation and temperature queries in an API using a Python Flask app:

/
Home page
/api/v1.0/precipitation
Daily precipitation totals for last year
/api/v1.0/stations
Active weather stations
/api/v1.0/tobs
Daily temperature observations for the WAIHEE weather station
/api/v1.0/trip/yyyy-mm-dd
Min, average & max temperatures for the range beginning with the provided start date through 08/23/17
/api/v1.0/trip/yyyy-mm-dd/yyyy-mm-dd
Min, average & max temperatures for the range beginning with the provided start - end date range
It consists of:

a SQLite database (Resources/Hawaii.sqlite)
a Flask app (sqlalchemy-challenge/app.py).


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
