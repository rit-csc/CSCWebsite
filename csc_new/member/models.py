from django.db import models
from django.contrib.auth.models import User

# TODO: EventResources needs to implemented to replace pages.models.ExamReview

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

# Event - defines an event | TODO: make this work with index.html and Google calendar
#	eventName - name of the event
#	eventTime - time of the event
class Event(models.Model):
	# id = models.AutoField(primary_key=True) # automatically created as long as no other primary key is defined
	eventName = models.CharField(max_length=80)
	eventTime = models.DateTimeField()
	
	def __str__(self):
		return self.eventName()

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
	
# CommitteeMembers - tracks who is members of committees
#	commMember - a foreign key to the member in a committee
#	commName - a foreign key to committee a member is a part of
class CommitteeMember(models.Model):
	# id = models.AutoField(primary_key=True) # automatically created as long as no other primary key is defined
	commMember = models.ForeignKey(Member)
	commName = models.ForeignKey(Committee)
	