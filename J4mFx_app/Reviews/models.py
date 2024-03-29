from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


"""Reviews model"""
class Reviews(models.Model):
	title = models.CharField(max_length=50)
	content =models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='Reviews_img')


	def __str__(self): 
		return self.title

	def get_absolute_url(self):
	    return reverse('review-detail',kwargs={'pk': self.pk} )	