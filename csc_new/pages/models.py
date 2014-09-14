from django.db import models
from django.utils.encoding import force_bytes

# dependent on icalendar package - pip install icalendar
from icalendar import Calendar, Event, vDatetime
from datetime import datetime
import urllib.request, urllib.error, urllib.parse
import os
from csc_new import settings

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
