from django.db import models
from  basemodel.models import BaseAbstractModel
# Create your models here.

class Incident(BaseAbstractModel):
    """ Incident model  """
    place = models.CharField(max_length=50,blank=False, null=False)
    personal_number = models.CharField(max_length=12,blank=False, null=False)
    description = models.TextField(max_length=500,blank=False, null=False)
    action = models.TextField(max_length=500,blank=True, null=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)

    #all this are to filled from code behind
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
