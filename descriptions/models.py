from django.db import models
from  basemodel.models import BaseAbstractModel

class DescriptionComparision(BaseAbstractModel):
    """ Description Comparision Model  """
    first_description = models.CharField(max_length=500,blank=False, null=False)
    second_description = models.CharField(max_length=500,blank=False, null=False)

    def __str__(self):
        """ Return a string representation of our description """
        return "{}".format(self.first_description)
