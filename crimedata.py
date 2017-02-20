import os, sys
import pandas as pd
from datetime import datetime
import numpy as np

def get_line_sum(fileObject):
    line_sum = 0
    with open(fileObject) as open_fileObject:
        for line in open_fileObject:
            line_sum += 1
    return line_sum

class crime_data:
    def __init__(self, Crime_file, Crime_dump):
        self.Crime_file = Crime_file
        self.Crime_dump = Crime_dump
        self.columns = ['Primary Type','Date']
        self.date_obj = "%m/%d/%Y %I:%M:%S %p"
        self.Crime_DF = pd.DataFrame(columns = self.columns)

    def get(self):
        if(not os.path.isfile(self.Crime_dump)):
            #6251550 number of crime records
            #chunking iterator
            chunks = pd.read_csv(self.Crime_file, chunksize=10000)

            #chunking loop
            for piece in chunks:
                #import data into new DF using columns [Primary Type, Date]
                frames = [self.Crime_DF,piece[self.columns]]
                self.Crime_DF = pd.concat(frames)

            self.Crime_DF['Date'] = pd.to_datetime(self.Crime_DF.Date, format=self.date_obj)
            self.Crime_DF.sort_values('Date', ascending=True,inplace=True)
            self.Crime_DF.reset_index(drop=True, inplace=True)
            #dumps to file
            self.Crime_DF.to_csv(self.Crime_dump, sep=',', header=True)


####TESTING##
##Crime_file = r"Crimes_-_2001_to_present.csv"
##Crime_dump = 'Crime.csv'
##CD = crime_data(Crime_file, Crime_dump)
##CD.get()
##del CD
