import os.path
import main
import datetime

from datetime import timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#creates private maths study event on 30/11/24 from 09:00 to 17:00
def createEvent(service, eventName, start, end, date, colour):
   event = {
  'summary': eventName,
  'start': {
    'dateTime': str(date) + 'T' + start,
    'timeZone': 'Europe/London',
  },
  'end': {
    'dateTime': str(date) + 'T' + end,
    'timeZone': 'Europe/London',
  },
  'colorId' : colour,
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=1'
  ],
   }
   event = service.events().insert(calendarId='primary', body=event).execute()
   print ('Event created: %s' % (event.get('htmlLink')))

def organisePrivates(service):
   today = datetime.date.today()
   # First array in private sessions is the start time and second array has the corresponding end time 
   privateSessions= [["08:40:00-00:00", "09:40:00-00:00","12:00:00-00:00"], ["09:40:00-00:00", "10:40:00-00:00","13:00:00-00:00"]]
   #Will only organise private sessions if there are 2 or more
   if len(privateSessions[0]) >= 2:
      #creates private sessions based on when private slots are
      for i in range(0,2):
         start = privateSessions[0][i]
         end = privateSessions[1][i]
         eventName = "Maths Private Study " + str(i+1)
         date = datetime.date.today()
         createEvent(service, eventName, start, end, date, "9")
      count = len(privateSessions[0])
      print(count)
      #Adds extra revision slots if there are more than 2 private study sessions
      for i in range(2,count):
         start = privateSessions[0][i]
         end = privateSessions[1][i]
         eventName = "Revision Session" + str(i-1)
         dateNum = str(int(today.strftime("%d")) + 1)
         print(dateNum)
         createEvent(service, eventName, start, end, today, "5")


def incrementDay(day):
   today = datetime.date.today()
   dateNum = str(int(today.strftime("%d")) + 1)
   print(dateNum)