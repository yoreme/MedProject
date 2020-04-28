from django.db import models
from datetime import datetime, date
from  basemodel.models import BaseAbstractModel
from utils.enum import  (MALE,SEXS,RISK,INCIDENT_CATEGORIES)
import uuid

# Create your models here.
# Status, Place, CreatedDate, EventDate, Ward, Description, 
# Category[risk,incident,adverseEvent], Gender, ClassificationLevel1, ClassificationLevel2, ClassificationLevel3

class Incident(BaseAbstractModel):
    """ Incident model  """
    place = models.CharField(max_length=50,blank=False, null=False)
    personal_number = models.CharField(max_length=12,blank=True, null=False)
    patient_firstname = models.CharField(max_length=12,blank=True, null=False)
    patient_lastname = models.CharField(max_length=12,blank=True, null=False)
    
    gender =models.CharField(max_length=10, default=MALE, choices=SEXS, null=True, blank=True)
    event_date=models.CharField(max_length=12,blank=False, null=False)
    category = models.CharField(max_length=20, default=RISK, choices=INCIDENT_CATEGORIES, null=True, blank=True)

    ward = models.TextField(max_length=5000,blank=True, null=False)
    suggestion = models.TextField(max_length=5000,blank=True, null=False)
    description = models.TextField(max_length=5000,blank=False, null=False)
    action = models.TextField(max_length=5000,blank=True, null=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    
    #all this are to filled from code behind
    reference_number=models.UUIDField(max_length=100, blank=True, unique=True,default=uuid.uuid4, editable=False)
    ip_address=models.CharField(max_length=50,blank=False, null=False)
    latitude=models.CharField(max_length=40,blank=False, null=False)
    longitude=models.CharField(max_length=40,blank=False, null=False)
    country_name=models.CharField(max_length=20,blank=False, null=False)
    country_code=models.CharField(max_length=20,blank=False, null=False)
    city=models.CharField(max_length=20,blank=False, null=False)
    region=models.CharField(max_length=20,blank=False, null=False)

    def __str__(self):
        """ Return a string representation of our incident """
        return "{}".format(self.personal_number)

