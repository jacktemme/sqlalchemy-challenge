Module 10 Challenge

This repository contains a climate analysis on Honolulu, Hawaii in terms of temperature and percipitation levels. The data for this analysis came from the hawaii.sqlite fild found in the Resources folder along with 2 other csv files used for table reference. Analysis for this data can be found in the climate_starter.ipynb file where SQLAlchemy was used to set up table classes and establish queries, while the matplot library was used to visually present the findings. In the app.py file the Python library Flask was then used to create an API where different routes were set up to access certain aspects of the data. Through this API you could look at a list of weather stations, temperature and perciptation data in the last year of recordings, and then the minimum, maximum, and average rainfall for the data ranges inputted by the user.


ChatGpt was reference on how to check if the inputted dates in the API endpoint were formatted correctly, so an error could be presented to the user if there was a mistake:

 Check if start and end dates are in correct format (YYYY-MM-DD)
        dt.strptime(start, '%Y-%m-%d')
        dt.strptime(end, '%Y-%m-%d')
