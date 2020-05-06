from django.db import models
import datetime
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Intern(models.Model):
	comp_name = models.CharField(max_length=30)
	job = models.CharField(max_length=30)
	desc = models.CharField(max_length=100)
	location= models.CharField(max_length=300,default="Work from home")
	stip=models.IntegerField(default=0)
	applyby=models.DateField(default=datetime.date.today)
	sdate=models.DateField(default=datetime.date.today)
	def __str__(self):
		return self.comp_name
	@property
	def is_past_due(self):
		return date.today() < self.sdate
    	

class Signup1(models.Model):
	full_name = models.CharField(max_length=30)
	gender = models.CharField(max_length=10)
	phone_no = models.IntegerField( validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
	status = models.CharField(max_length=30,default="Pending")
	email= models.EmailField()
	internship=models.ForeignKey(Intern,on_delete=models.CASCADE)
	resume_file = models.FileField(upload_to='resume_folder')
	class Meta:
		unique_together=["full_name","email","internship"]
	def __str__(self):
		return self.full_name


