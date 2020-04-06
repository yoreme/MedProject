from django.db import models
from django.conf import settings
from basemodel import baseabstractmodel
# Create your models here.
<<<<<<< HEAD


class Incident(baseabstractmodel):
    """Incident object"""
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=75,blank=True, null=True)
    phone_no = models.CharField(max_length=15,blank=False)
    email = models.EmailField(max_length=255,blank=True, null=True)
    Date_of_birth=models.DateField(blank=True, null=True)
    contactgroup = models.ForeignKey('contactgroups.ContactGroup', on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.phone_no
=======
class ReportIncident(models.Model):
    place = models.CharField(max_length=50, blank=False)

    personalNumber = models.CharField(blank=False, max_length=12)
    time = models.DateField(blank=False, null=True, default=None)

    description = models.TextField(max_length=500, blank=False)
    action = models.TextField(max_length=500, blank=True)

    image = models.ImageField(upload_to='images/', blank=True)

>>>>>>> 653b1677a7078d1c626b05cd075464d437cb12b9
