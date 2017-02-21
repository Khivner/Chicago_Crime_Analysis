import os, sys, csv
from datetime import datetime, timedelta

class cycle_bin:
    def __init__(self, LD, Crime_dump, moon_phase):
        self.delta = timedelta(days=14)
        self.LD = LD
        self.Crime_dump = open(Crime_dump,'r')
        self.LD_format = "%Y %b %d %H:%M"
        self.CD_format = "%Y-%m-%d %H:%M:%S"
        self.Data = [0 for x in range(28)]
        self.moon_phase = moon_phase

    def avg_data(self):
        for x in range(28):
            self.Data[x] = round(float(self.Data[x]/len(self.LD.Data[self.moon_phase])))
            
    #bins data for each 24 hour period symmetrically around one lunar cycle
    #start_date/end_date refer to cycle start/end, date refers to lunar event
    def bin_cycle(self, reader, start_date, end_date, date):

        crime_date = datetime.strptime(next(reader)[2], self.CD_format)
        for n in range(28):
            day_start = datetime.strptime(date, self.LD_format)-self.delta+timedelta(days=n)
            day_end = datetime.strptime(date, self.LD_format)-self.delta+timedelta(days=n+1)
            
            while(crime_date < day_end):
                #print(crime_date)
                if(crime_date > start_date):
                    self.Data[n] += 1
                crime_date = datetime.strptime(next(reader)[2], self.CD_format)
                    ##Note while the last crime date pulled in this loop will be 
                    ##essentially thrown away, this should not affect the data
                    ##because the average lunar cycle is about 29.14 days
                    ##and we are only considering a 28 day cycle
                    ##so this value would most likely have been thrown away anyways
        
    #runs bin cycle for all lunar cycles           
    def bin_data(self):
        with self.Crime_dump as file:
            reader = csv.reader(file)
            #skips header row
            #For python 3 ignore the tutorials on csv reader.next
            #Use next(reader) instead the above will not work
            next(reader)
            
            #LD.Data[1] is where all the full moon event dates are stored
            for date in self.LD.Data[self.moon_phase]:
                print(date)
                #start and end dates for the current cycle
                start_date = datetime.strptime(date, self.LD_format)-self.delta
                end_date = datetime.strptime(date, self.LD_format)+self.delta
                print(start_date)
                print(end_date)
                #bin for current cycle
                self.bin_cycle(reader, start_date, end_date, date)
                
        #averages data over all observed lunar cycles
        self.avg_data()

##TESTING##
##from lunardata import lunar_data
##Crime_dump = 'Crime.csv'
##Lunar_Start = r"2001 Jan 01 01:01"
##Lunar_End = r"2017 Jan 01 01:01"
##LD = lunar_data(r"TEST.csv",Lunar_Start, Lunar_End)
##LD.get()
##CB = cycle_bin(LD, Crime_dump)
##CB.bin_data()
##sum = 0
##for x in CB.Data:
##    sum += x
##print(sum)
