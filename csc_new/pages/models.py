from django.db import models

# dependent on icalendar package - pip install icalendar
from icalendar import Calendar, Event, vDatetime
from datetime import datetime
import urllib.request, urllib.error, urllib.parse

# Create your models here.

class RenderableEvent:
	def __init__(self, summ, sdate, edate, d):
		self.summary = summ
		self.start_date = sdate
		self.end_date = edate
		self.desc = d

class RenderableEvents:
	events = []

	@classmethod
	def getEvents(self):
		icalFile = urllib.request.urlopen('http://www.google.com/calendar/ical/calendar%40csc.cs.rit.edu/public/basic.ics')
		ical = Calendar.from_ical(icalFile.read())
		for thing in ical.walk():
			eventtime = thing.get('dtstart')
			if thing.name == "VEVENT" and eventtime.dt.replace(tzinfo=None) > datetime.now():
				event = RenderableEvent(thing.get('summary'), eventtime.dt.replace(tzinfo=None), thing.get('dtend').dt.replace(tzinfo=None), thing.get('description'))
				self.events.append(thing)
		icalFile.close()
