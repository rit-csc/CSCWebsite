from django.db import models

# Create your models here.
class Member(models.Model):
	dce = models.CharField(max_length=10, primary_key=True)
	name = models.CharField(max_length=80)
	email = models.EmailField()
	status = # add levels here
	inGoodStanding = models.BoolField()
	
class Events(models.Model):
	name = models.CharField(max_length=80)
	attendee = models.ForeignKey(Member)
	