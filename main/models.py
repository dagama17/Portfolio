from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Profile(models.Model):
	first_name = models.CharField(max_length=255, null=False, blank=True)
	last_name = models.CharField(max_length=255, null=False, blank=True)
	specialty = models.CharField(max_length=255, null=False, blank=True)
	bio = models.TextField(max_length=255, blank=True)
	image = models.ImageField(upload_to="img", default='img/avatar.png')
	cv = models.FileField(upload_to="files")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.first_name

class Service(models.Model):
	title = models.CharField(max_length=255, blank=True)
	description = models.TextField()
	picture = models.ImageField(upload_to="img")
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	duration = models.CharField(max_length=255, blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Rating(models.Model):
	course = models.OneToOneField(Service, null=True, on_delete=models.CASCADE)
	score = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

	def __str__(self):
		return str(self.score)


class Agent(models.Model):
	first_name = models.CharField(max_length=255, null=False, blank=True)
	last_name = models.CharField(max_length=255, null=False, blank=True)
	number = models.CharField(max_length=255, null=False, blank=True)
	email = models.EmailField(max_length = 254, blank=True)
	image = models.ImageField(upload_to="img", default='img/avatar.png')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.first_name + " " + self.last_name)