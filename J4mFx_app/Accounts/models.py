import os
import secrets
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


'''User profile model'''
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	followers = models.ManyToManyField(User, blank=True, related_name='followers')
	profile_pc = models.ImageField(default='default.jpg', upload_to='profile_pcs')

	def __str__(self):
		return f'{self.user.username} Profile'

	'''image resizing'''
	def save(self, **kwargs):
		super().save()
		# randam_name = secrets.token_hex(12)
		# _, f_ext = os.path.splitext(self.profile_pc.path.name)
		# profile_new_name = randam_name + f_ext
		# picture_path = os.path.join(self.profile_pc.path, profile_new_name)
		img = Image.open(self.profile_pc.path)

		if img.height > 300 or img.width >300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.profile_pc.path)
