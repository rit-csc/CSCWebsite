from django.db import models

# TODO: EventResources needs to implemented to replace pages.models.ExamReview

# MemberType - defines member types
# 	typeName - the human-readable name of the type
class MemberType(models.Model):
	# id = models.AutoField(primary_key=True) # automatically created as long as no other primary key is defined
	typeName = models.CharField(max_length=20)
	# benefits and other stuff here

# Member - defines a member (finally!)
#	dce - primary key that is also RIT's DCE
#	name - the name of the member
#	email - the email of the member
#	type - the member type	
class Member(models.Model):
	# TODO: add more (or less, I'm a source file.  I don't run the club)
	# BASIC = 0
	# PREMIUM = 1
	# EBOARD = 2
	# MEMBER_STATUS = (
		# (BASIC, 'Basic'),
		# (PREMIUM, 'Premium'),
		# (EBOARD, 'E-Board'),
	# )

	dce = models.CharField(max_length=10, primary_key=True)
	name = models.CharField(max_length=80)
	email = models.EmailField()
	type = models.ForeignKey(MemberType)

# Event - defines an event | TODO: make this work with index.html and Google calendar
#	eventName - name of the event
#	eventTime - time of the event
class Event(models.Model):
	# id = models.AutoField(primary_key=True) # automatically created as long as no other primary key is defined
	eventName = models.CharField(max_length=80)
	eventTime = models.DateTimeField()

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
class CommitteeMembers(models.Model):
	# id = models.AutoField(primary_key=True) # automatically created as long as no other primary key is defined
	commMember = models.ForeignKey(Member)
	commName = models.ForeignKey(Committee)
	