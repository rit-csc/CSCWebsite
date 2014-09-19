from django.db import models
from django.contrib.auth.models import User

# TODO: EventResources needs to be implemented to replace pages.models.ExamReview

# MemberType - defines member types
# 	typeName - the human-readable name of the type
class MemberType(models.Model):
	# id = models.AutoField(primary_key=True) # automatically created as long as no other primary key is defined
	typeName = models.CharField(max_length=20)
	# TODO: benefits and other stuff here
	
	def __str__(self):
		return self.typeName

# Member - defines a member (finally!)
#	user - holds name, username(dce), email
#	type - the member type
class Member(models.Model):
	user = models.OneToOneField(User) # covers name and email
	type = models.ForeignKey(MemberType)

	def committee_memberships(self):
		return CommitteeMembership.objects.filter(commMember=self.pk)

	def event_logins(self):
		return EventLogin.objects.filter(attendee=self.pk)

	# TODO: FIGURE OUT HOW TO DO THIS BETTER
	def events_attended(self):
		events = []
		for login in event_logins(self):
			events.append(Event.objects.get(pk=login.eventNo.pk))
		return events

# Event - defines an event | TODO: make this work with index.html and Google calendar
#	eventName - name of the event
#	eventTime - time of the event
class Event(models.Model):
	# id = models.AutoField(primary_key=True) # automatically created as long as no other primary key is defined
	eventName = models.CharField(max_length=80)
	eventTime = models.DateTimeField()
	
	def __str__(self):
		return self.eventName()

	def event_logins(self):
		return EventLogin.objects.filter(eventNo=self.pk)

# EventLogin - tracks members who sign in at events
#	eventNo - a foreign key to the event signed into
#	attendee - a foreign key to the member who signed in
class EventLogin(models.Model):
	# id = models.AutoField(primary_key=True) # automatically created as long as no other primary key is defined
	eventNo = models.ForeignKey(Event)
	attendee = models.ForeignKey(Member)
	
# Committee - defines a committee
#	commName - the name of the committee
#	chair - a foreign key to a member who is the chair of this committee
#	commEmail - the mailing list of the committee
class Committee(models.Model):
	# id = models.AutoField(primary_key=True) # automatically created as long as no other primary key is defined
	commName = models.CharField(max_length=80)
	chair = models.ForeignKey(Member)
	commEmail = models.EmailField()

	def member_list(self):
		return CommitteeMembership.objects.filter(comm=self.pk)
	
# CommitteeMembership - represents a members membership in a committees (many-to-many mapping)
#	commMember - a foreign key to the member in a committee
#	commName - a foreign key to committee a member is a part of
class CommitteeMembership(models.Model):
	# id = models.AutoField(primary_key=True) # automatically created as long as no other primary key is defined
	commMember = models.ForeignKey(Member)
	comm = models.ForeignKey(Committee)
	