from django.db import models
from django.conf import settings
from basemodel import baseabstractmodel
# Create your models here.

class Incident(baseabstractmodel):
    place = models.CharField(max_length=50, blank=False)

    personalNumber = models.CharField(blank=False, max_length=12)
    time = models.DateField(blank=False, null=True, default=None)

    description = models.TextField(max_length=500, blank=False)
    action = models.TextField(max_length=500, blank=True)

    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.phone_no
