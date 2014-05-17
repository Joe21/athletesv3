from django.db import models

# Create your models here.
class Athlete(models.Model):
	RECOMMENDATIONS = (
		('a', 'Hire Joe IMMEDIATELY!'),
		('b', 'Hire Joe NOW!')
		)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	sport = models.CharField(max_length=50)
	recommendation = models.CharField(max_length=1, choices=RECOMMENDATIONS)

	def __unicode__(self):
		return self.first_name