from django.db import models
from datetime import datetime, date
from  basemodel.models import BaseAbstractModel
import uuid

# Create your models here.

class Incident(BaseAbstractModel):
    """ Incident model  """
    place = models.CharField(max_length=50,blank=False, null=False)
    personal_number = models.CharField(max_length=12,blank=False, null=False)
    patient_firstname = models.CharField(max_length=12,blank=False, null=False)
    patient_lastname = models.CharField(max_length=12,blank=False, null=False)
    suggestion = models.TextField(max_length=5000,blank=False, null=False)

     # Login Status
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    SEXS = ((MALE, 'MALE'),
            (FEMALE, 'FEMALE')
            )

    patient_sex =models.CharField(max_length=10, default=MALE, choices=SEXS, null=True, blank=True)
    description = models.TextField(max_length=5000,blank=False, null=False)
    action = models.TextField(max_length=5000,blank=True, null=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    incident_date=models.DateTimeField(default=datetime.now(), blank=False, null=False)

    # Login Status
    RISK = 'Risk'
    NEARMISS = 'Near miss'
    ADVERSEEVENT = 'Adverse Event'
    INCIDENT_TYPES = ((RISK, 'Risk'),
                (NEARMISS, 'Near miss'),
                (NEARMISS, 'Adverse Event'),
                )
    
    # incident_types = (
    #                     (1, "Risk"),
    #                     (2, "Near miss"),
    #                     (3, "Adverse Event"),
    #                 )
    # type = models.PositiveSmallIntegerField(choices=incident_types, default=1)
    incident_type = models.CharField(max_length=10, default=RISK, choices=INCIDENT_TYPES, null=True, blank=True)


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

