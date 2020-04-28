from django.db import models
from  basemodel.models import BaseAbstractModel
# Create your models here.

class First_Category(BaseAbstractModel):
    """ Incident Management FIrst Category model  """
    name = models.CharField(max_length=50,blank=False, null=False)

    def __str__(self):
        """Return a string representation of our user"""
        return "{}".format(self.name)


class Second_Category(BaseAbstractModel):
    """ Incident Management Second Category model   """
    name = models.CharField(max_length=50,blank=False, null=False)
    firstcategory = models.ForeignKey('lookups.First_Category', on_delete=models.CASCADE,blank=True, null=True)


    def __str__(self):
        """Return a string representation of our user"""
        return "{}".format(self.name)



class Third_Category(BaseAbstractModel):
    """ Incident Management Third Category model   """
    name = models.CharField(max_length=50,blank=False, null=False)
    first_category = models.ForeignKey('lookups.First_Category',related_name='firstcategory', on_delete=models.CASCADE,blank=True, null=True)
    secondcategory = models.ForeignKey('lookups.Second_Category',related_name='secondcategory',on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        """Return a string representation of our user"""
        return "{}".format(self.name)

