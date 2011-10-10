from django.db import models
from chihuo.people.models import Person
from chihuo.restaurants.models import Shop

class Group(models.Model):
	members = models.ManyToManyField(Person)
		

class ChihuoEvent(models.Model):
	title = models.CharField(max_length=50)
	date = models.DateField()
	opacity = models.IntegerField()
	place = models.ForeignKey(Shop)
	description = models.TextField(max_length=200)
	initiator = models.ForeignKey(Person)
	group = models.ForeignKey(Group)
	def __unicode__(self):
		return '%s' % (self.title)


