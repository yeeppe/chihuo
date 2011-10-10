from django.db import models
from chihuo.stats.models import UserStat
from chihuo.posts.models import Post
from chihuo.commentSystem.models import Comment

GENDER_CHOICES = (
		(u'M', u'Male'),
		(u'F', u'Female'),
		(u'O', u'Other'),
)

class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
	email = models.EmailField()
	register_date = models.DateField()
	user_stat = models.ForeignKey(UserStat)
	comments = models.ManyToManyField(Comment)
	#headshot = models.ImageField(upload_to="static/users/headshot")
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

class Editor(Person):
	posts = models.ManyToManyField(Post)
	
class Contributor(Person):
	posts = models.ManyToManyField(Post)
	