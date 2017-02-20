#Built in Python 3.6.0
#Dependency on html5lib make sure to install that too

import os, sys, csv
from bs4 import BeautifulSoup
import requests
from datetime import datetime

class lunar_data:
    def __init__(self, file, Start, End):
        self.Data = []
        self.file = file
        self.Start = Start
        self.End = End
        self.LD_format = "%Y %b %d %H:%M"
        
    def generate_link(self, date_str):
        date_obj = datetime.strptime(date_str, self.LD_format)
        link = "http://aa.usno.navy.mil/cgi-bin/aa_phases.pl?year=" + str(date_obj.year) + "&month=" + str(date_obj.month) +"&day=" + str(date_obj.day) + "&nump=99&format=t"
        return link

    ##Strips dates that we do not have crime data for (beyond end date)
    def remove_extra(self, phase):
        enddate_obj = datetime.strptime(self.End, self.LD_format)
        for date in self.Data[phase]:
            date_obj = datetime.strptime(date, self.LD_format)
            if(date_obj > enddate_obj):
                self.Data[phase] = self.Data[phase][:self.Data[phase].index(date)]
                ##Cut first and last lunar event date
                ##to ensure a full set of data for each lunar cycle
                self.Data[phase] = self.Data[phase][1:-1]
                return
            
    #dumps data to csv file 
    def dump(self, data):
        with open(self.file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.Data)
                                
    def GetLunarData(self):
        link_list = ["http://aa.usno.navy.mil/cgi-bin/aa_phases.pl?year=2013&month=6&day=1&nump=99&format=t","http://aa.usno.navy.mil/cgi-bin/aa_phases.pl?year=2015&month=6&day=1&nump=99&format=t"]
        end_date_obj = datetime.strptime(self.End, self.LD_format)
        #Last quarter
        L1 = 'Last Quarter'
        last_quarter = []
        #New moon
        L2 = 'New Moon'
        new_moon = []
        #First quarter
        L3 = 'First Quarter'
        first_quarter = []
        #Full moon
        L4 = 'Full Moon'
        full_moon = []

        html = self.generate_link(self.Start)
        current = datetime.strptime(self.Start, self.LD_format)
        while(current < end_date_obj):
            #grabs the html code of the page containing our lunar cycle data
            html_req = requests.get(html).text
            #creates a beautiful soup object
            soup = BeautifulSoup(html_req, 'html5lib')

            #gets all table cell data, all odd cells will be moon phase all even cells date/time
            LunarData = soup.find_all('td')

            #strips <td> and </td> from each cell returns data as a list of strings
            data = [str(td)[4:-5] for td in LunarData]
            
            #These loops separate the dates into 4 lists based on the phase of the moon at that date
            #this is necessary because we will want to examine each unique moon phase
            for i in range(1,199,2):
                if data[i-1] == L1:
                    last_quarter.append(data[i])
                if data[i-1] == L2:
                    new_moon.append(data[i])
                if data[i-1] == L3:
                    first_quarter.append(data[i])
                if data[i-1] == L4:
                    full_moon.append(data[i])        

            current = datetime.strptime(data[-1], self.LD_format)
            html = self.generate_link(data[-1])
            print(data[-1])
        #returns a list of the moon phase data lists
        self.Data = [first_quarter,full_moon,last_quarter,new_moon]
        for phase in range(4):
            self.remove_extra(phase)
        

    

    #loads in Lunar data from csv if the file exists, or scrapes from the online database
    def get(self):
        if(os.path.isfile(self.file)):
            with open(self.file, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    self.Data.append(row)
        else:
            self.GetLunarData()
            self.dump(self.Data)
        

##TESTING##
##Lunar_Start = r"2001 Jan 01 01:01"
##Lunar_End = r"2017 Jan 01 01:01"
##LD = lunar_data(r"TEST.csv",Lunar_Start, Lunar_End)
##LD.get()
