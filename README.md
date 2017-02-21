# Chicago_Crime_Analysis

##Objective:
Analyze a data set of crime reports in Chicago, IL, spanning from January 2001 to January 2017.  This data was obtained from [https://catalog.data.gov/dataset/crimes-2001-to-present-398a4](here) at data.gov in csv format. The first analysis attempted to find a correlation between lunar phases and reported crime rates. To do this we consider a 28 day lunar cycle and center each cycle around the event of interest, in the first case a full moon event. Data for the lunar cycles was scraped from the U.S. Naval Observatory Astronomical Applications Department website. Data for each cycle was binned using 24 hour intervals to observe number of daily reported crimes, then an average was taken for each day in the cycle over all considered cycles.

##Getting Started
To run this project the following are required:
* The crime reports data set for the city of Chicago located [https://catalog.data.gov/dataset/crimes-2001-to-present-398a4](here).
* Python 3.6
* Python Libraries: pandas, beautifulsoup4, html5lib, requests, matplotlib, numpy

