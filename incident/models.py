from django.db import models
from django.conf import settings
from basemodel import baseabstractmodel
# Create your models here.

class Incident(baseabstractmodel):
    place = models.CharField(max_length=50, blank=False)

    personalNumber = models.CharField(blank=False, max_length=12)

    description = models.TextField(max_length=500, blank=False)
    action = models.TextField(max_length=500, blank=True)

    image = models.ImageField(upload_to='images/', blank=True)

    #all this are to filled from code behind
    ip_address=models.CharField(max_length=50,blank=False, null=False)
    latitude=models.CharField(max_length=40,blank=False, null=False)
    longitude=models.CharField(max_length=40,blank=False, null=False)
    country_name=models.CharField(max_length=20,blank=False, null=False)
    country_code=models.CharField(max_length=20,blank=False, null=False)
    city=models.CharField(max_length=20,blank=False, null=False)
    region=models.CharField(max_length=20,blank=False, null=False)

    def __str__(self):
        return self.personalNumber
