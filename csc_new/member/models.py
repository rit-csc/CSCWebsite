from django.db import models
#from django.contrib.auth.models import AbstractUser, UserManager

# MemberType - defines member types
# 	typeName - the human-readable name of the type
class MemberType(models.Model):
	REQUIRED_FIELDS = ['typeName']

	typeName = models.CharField(max_length=20, default="Base")
	# TODO: benefits and other stuff here
	
	def __str__(self):
		return self.typeName + " Member"

class Member(AbstractUser):
	objects = UserManager()
	username = models.CharField(max_length=10, required=True)
	name = models.CharField(max_length=10, required=True)
	bio = models.CharField(max_length=10, required=False, default="")

class Tutor(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	
class Officer(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	position = models.CharField(max_length=10, required=True)
	
class Shift(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	start = models.TimeField(required=True)
	end = models.TimeField(requried=True)
	day = models.DateField(required=True)
	
# Member - defines a member
#	user - holds name, username(dce), email
#	type - the member type
#class Member(AbstractUser):
#	REQUIRED_FIELDS = ['memberType', 'email']
#
#	# Default User Manager being attached
#	objects = UserManager()
#
#	# memberType = models.ForeignKey(MemberType)
#	memberType = models.CharField(max_length=20, default="Base")
#
#	# def __str__(self):
#	# 	return self.memberType + "Member No. " + self.pk
#
#	# Committees for which this Member has a CommitteeMembership.
#	# (Use the ManyToMany relationship to return all related committees.)
#	def _committees_member_of(self):
#		return self.committee_set.all()
#	committees = property(_committees_member_of)

#	# Events for which this Member has an EventLogin.
#	# (Use the ManyToMany relationship to return all related events.)
#	def _events_attended(self):
#		return self.event_set.all()
#	events = property(_events_attended)

# Event - defines an event
#	name - name of the event
#	start_time - time of the event
# 	loc	- location of the event
class Event(models.Model):
	REQUIRED_FIELDS = ['name']

	name = models.CharField(max_length=80)
	start_time = models.DateTimeField(null=True)
	loc = models.CharField(max_length=80, null=True)

	# ManyToMany relationship, with EventLogin as the intermediate model.
	# In this way, EventLogin is associated with the ManyToManyField and can
	# 	store additional information about the relationship.
	attendees = models.ManyToManyField(Member, through='EventLogin')
	
	def __str__(self):
		return self.name

# EventLogin - intermediate model used to define the ManyToMany
# 					relationship between members and events
#	event - a foreign key to the event signed into
#	attendee - a foreign key to the member who signed in
class EventLogin(models.Model):
	REQUIRED_FIELDS = ['event', 'attendee']

	event = models.ForeignKey(Event)
	attendee = models.ForeignKey(Member)

	# Can add additional fields here...
	
# Committee - defines a committee
#	name - the name of the committee
#	chair - the member who is the chair of this committee
#	email - the mailing list for the committee
class Committee(models.Model):
	REQUIRED_FIELDS = ['name', 'email']

	name = models.CharField(max_length=80)
	email = models.EmailField()
	chair = models.ForeignKey(Member, related_name="committee_chair", null=True)

	# ManyToMany relationship, with CommitteeMembership as the intermediate model.
	# In this way, CommitteeMembership is associated with the ManyToManyField and can
	# 	store additional information about the relationship.
	members = models.ManyToManyField(Member, through='CommitteeMembership')
	
# CommitteeMembership - intermediate model used to define the ManyToMany
# 						relationship between members and committees
#	member - a foreign key to the member in a committee
#	committee - a foreign key to committee a member is a part of
class CommitteeMembership(models.Model):
	REQUIRED_FIELDS = ['member', 'committee']

	member = models.ForeignKey(Member)
	committee = models.ForeignKey(Committee)

	# Automatically set to the current time when the object is first created.
	date_joined = models.DateField(auto_now_add=True)
	
