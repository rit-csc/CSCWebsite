from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# MemberType - defines member types
# 	typeName - the human-readable name of the type
class MemberType(models.Model):
	REQUIRED_FIELDS = ['typeName']

	typeName = models.CharField(max_length=20, default="Base")
	# TODO: benefits and other stuff here
	
	def __str__(self):
		return self.typeName + " Member"

# Member - defines a member
#	user - holds name, username(dce), email
#	type - the member type
class Member(AbstractUser):
	REQUIRED_FIELDS = ['memberType']

	# Default User Manager being attached
	objects = UserManager()

	# memberType = models.ForeignKey(MemberType)
	memberType = models.CharField(max_length=20, default="Base")

	# def __str__(self):
	# 	return self.memberType + "Member No. " + self.pk

	# Committees for which this Member has a CommitteeMembership.
	# (Use the ManyToMany relationship to return all related committees.)
	def committees_member_of(self):
		return self.committee_set.all()

	# Return all EventLogins for this Member.
	def event_logins(self):
		return EventLogin.objects.filter(attendee=self.pk)

	# Events for which this Member has an EventLogin.
	# (Use the ManyToMany relationship to return all related events.)
	def events_attended(self):
		return self.event_set.all()

# Event - defines an event
#	name - name of the event
#	time - time of the event
# 	loc	- location of the event
class Event(models.Model):
	REQUIRED_FIELDS = ['name']

	name = models.CharField(max_length=80)
	time = models.DateTimeField()
	loc = models.CharField(max_length=80)

	# ManyToMany relationship, with EventLogin as the intermediate model.
	# In this way, EventLogin is associated with the ManyToManyField and can
	# 	store additional information about the relationship.
	attendees = models.ManyToManyField(Member, through='EventLogin')
	
	def __str__(self):
		return self.name

# EventLogin - intermediate model used to define the ManyToMany
# 					relationship between members and events
#	eventNo - a foreign key to the event signed into
#	attendee - a foreign key to the member who signed in
class EventLogin(models.Model):
	REQUIRED_FIELDS = ['eventNo', 'attendee']

	eventNo = models.ForeignKey(Event)
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

	# Can add additional fields here...
	date_joined = models.DateField()
	
