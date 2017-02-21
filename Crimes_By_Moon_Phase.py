#Built in Python 3.6.0
#Dependency on html5lib make sure to install that too

import os, sys
from datetime import datetime, timedelta
from lunardata import lunar_data
from crimedata import crime_data
from daybin import cycle_bin
from graphdata import generate_graph

#Start program
#Choose the Lunar phase to correlate data with
#0 = First Quarter Moon
#1 = Full Moon
#2 = Last Quarter
#3 = New Moon
moon_phase = 1

#CD constructor args
Crime_File = r"Crimes_-_2001_to_present.csv"
Crime_dump = 'Crime.csv'

#LD constructor args
#start and end dates for scraping lunar data if dump file does not exist
Lunar_Start = r"2001 Jan 01 01:01"
Lunar_End = r"2017 Jan 01 01:01"
csv_file = 'Lunar_Data.csv'

#y range values for graphing
yrange = range(1050,1100,5)

#gets lunar data (scrape or archived dump file)
LD = lunar_data(csv_file, Lunar_Start, Lunar_End)
LD.get()
#gets data from the Crime_File obtained from data.gov
CD = crime_data(Crime_File, Crime_dump)
CD.get()
#free up the memory from CD since all data is now in Crime_dump file
del CD

#run binning algorithm
print("START")
bin_list = cycle_bin(LD, Crime_dump, moon_phase)
bin_list.bin_data()

#Generate visualization of bin'd and averaged data
graph = generate_graph(bin_list.Data, yrange, 'full_moon_results.png')
graph.make_fig()

