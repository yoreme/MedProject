from django.db import models
from django.conf import settings
from basemodel import baseabstractmodel
# Create your models here.


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