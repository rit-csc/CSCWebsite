from django.db import models
from django.utils.encoding import force_bytes
from django.utils import timezone

# dependent on icalendar package - pip install icalendar
from icalendar import Calendar, Event, vDatetime, LocalTimezone
from datetime import datetime, timedelta
import urllib.request, urllib.error, urllib.parse
import os
from csc_new import settings

import dateutil.rrule as rrule

# Create your models here.
class ExamReview(models.Model):	
	title = models.CharField(max_length=100)
	questions = models.FileField(upload_to="exam_reviews")
	answers = models.FileField(upload_to="exam_reviews")
		
	def __str__(self):
		return '%s' % (self.title)

	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, str(self.questions)))
		os.remove(os.path.join(settings.MEDIA_ROOT, str(self.answers)))
		super(ExamReview, self).delete(*args, **kwargs)

class Photo(models.Model):
	title = models.CharField(max_length=100)
	desc = models.CharField(max_length=255)
	src = models.FileField(upload_to="photos")

	def __str__(self):
		return self.title + " - " + self.desc

	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, str(self.src)))
		super(Photo, self).delete(*args, **kwargs)

# RenderableEvent - holds an event
class RenderableEvent:
	__slots__=('summary', 'start_date', 'start_time', 'end_time', 'desc', 'pureTime', 'location')

	def __init__(self, summ, sdate, stime, etime, d, stimePure, loc):
		self.summary = summ
		self.start_date = sdate
		self.start_time = stime
		self.end_time = etime
		self.desc = d
		self.pureTime = stimePure
		self.location = loc

	def __str__(self):
		return self.summary + " " + self.start_date + " "+ self.start_time + " "+ self.end_time + " " + self.location

# RenderableEvents - holds all events
class RenderableEvents:
	__slots__ = ('events')
	
	def __init__(self):
		self.events = []

	def getEvents(self):
		icalFile = urllib.request.urlopen('http://www.google.com/calendar/ical/calendar%40csc.cs.rit.edu/public/basic.ics')
		ical = Calendar.from_ical(icalFile.read())
	#	lt = LocalTimezone()
		offset = timedelta(hours=-5)
		for thing in ical.walk():
			eventtime = thing.get('dtstart')
			# if eventtime != None:
			# 	offset = lt.utcoffset(eventtime.dt)
			loc = thing.get('location')
			if ( loc== None) or (loc == "") or (loc == "TBD"):
				loc = "TBD"
			if thing.name == "VEVENT" and eventtime.dt.replace(tzinfo=None)+offset > datetime.today() - timedelta(days=1):
				event = RenderableEvent(thing.get('summary'), (eventtime.dt.replace(tzinfo=None)+offset).strftime("%m/%d/%Y"), \
					(eventtime.dt.replace(tzinfo=None)+offset).strftime("%I:%M %p"),\
					(thing.get('dtend').dt.replace(tzinfo=None)+offset).strftime("%I:%M %p"), thing.get('description'),\
					(eventtime.dt.replace(tzinfo=None)+offset), loc)
				inserted = False
				# TODO this can probably be improved in terms of efficiency.
				for i in range(len(self.events)): # this appears to orders our events by date! ... backwards.
					if self.events[i].pureTime < (eventtime.dt.replace(tzinfo=None)+offset):
						self.events.insert(i,event)
						inserted = True
						break
				if not inserted:
					self.events.append(event)
			elif thing.name == "VEVENT" and thing.get('RRULE') is not None:
				repeats = list(rrule.rrulestr(thing.get('RRULE').to_ical().decode('unicode_escape'), ignoretz=True, dtstart=datetime.now()))
				if(len(repeats) <= 0):
					continue
				#Remove after Fall Semester 2014
				if(thing.get('summary') == 'General Meeting!'):
					continue
				# # # # # # # # # # # # # # # # #
				self.events.append(RenderableEvent(thing.get('summary'), (repeats[0].replace(tzinfo=None)).strftime("%m/%d/%Y"), \
					(thing.get('dtstart').dt.replace(tzinfo=None)).strftime("%I:%M %p"), \
					(thing.get('dtend').dt.replace(tzinfo=None)).strftime("%I:%M %p"), thing.get('description'), \
					(repeats[0].replace(tzinfo=None)), loc))
		self.events = self.events[::-1] # reverse the list, because it was backwards by date!
		icalFile.close()

