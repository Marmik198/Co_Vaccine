from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,blank=True,null=True)
    firstName = models.CharField(max_length=100,blank=True)
    lastname = models.CharField(max_length=100,blank=True)
    aadhar = models.CharField(max_length=12,blank=True)
    contact = models.CharField(max_length=10,blank=True)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=30,blank=True)
    Flatno = models.CharField(max_length=200,blank=True)
    Address = models.CharField(max_length=200,blank=True)
    City = models.CharField(max_length=200,blank=True)
    State = models.CharField(max_length=200,blank=True)
    Country = models.CharField(max_length=50,blank=True)
    medical_issues = models.CharField(max_length=500,default="N.A.")
    current_symptom = models.CharField(max_length=500,blank=True,default="N.A.")
    covid_status = models.CharField(max_length=500,default="Negative")
    travel_history = models.CharField(max_length=500,default="No")
    date = models.DateField(blank=True,null=True,default=timezone.now)
    dose = models.CharField(max_length=500,blank=True)
    center = models.CharField(max_length=500,blank=True)
    desc = models.CharField(max_length=255,blank=True)
    image = models.ImageField(default='default.png',upload_to='appointment_verification')


    def __str__(self):
            return self.firstName + " " + self.lastname

