from django.db import models


class MyUser(models.Model):
	your_name = models.CharField(max_length=100,primary_key=True)
	password = models.IntegerField()
	

	def __str__(self):
		return self.your_name

class UserProfile(models.Model):
	user = models.ForeignKey(MyUser)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length = 300)
	phone = models.IntegerField()
	address = models.CharField(max_length=30)

	def __str__(self):
		return self.name

