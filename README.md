# Chicago_Crime_Analysis

##Objective:
Analyze a data set of crime reports in Chicago, IL, spanning from January 2001 to January 2017.  This data was obtained from [here](https://catalog.data.gov/dataset/crimes-2001-to-present-398a4) at data.gov in csv format. The first analysis attempted to find a correlation between lunar phases and reported crime rates. To do this we consider a 28 day lunar cycle and center each cycle around the event of interest, in the first case a full moon event. Data for the lunar cycles was scraped from the U.S. Naval Observatory Astronomical Applications Department website. Data for each cycle was binned using 24 hour intervals to observe number of daily reported crimes, then an average was taken for each day in the cycle over all considered cycles.

##Getting Started
To run this project the following are required:
* The crime reports data set for the city of Chicago located [here](https://catalog.data.gov/dataset/crimes-2001-to-present-398a4).(make sure to download the csv file)
* Python 3.6
* Python Libraries: Use the following in the command line 
```pip install pandas beautifulsoup4 html5lib requests matplotlib numpy```

###After cloning the repo 
1. Place place the Crimes_-_2001_to_present.csv file into the root project directory 
2. Then just run the Crimes_By_Moon_Phase.py file with Python 3.6. 
3. (optional) The analysis currently runs for full moon events but if you're interested in first quarter moon, last quarter moon, or new moon periods you can change the value of the moon_phase variable in the Crimes_By_Moon_Phase.py to the appropriate integer value representing the desired phase (values are noted in the comments immediately above the variable).

##Results
