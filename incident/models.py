from django.db import models

# Create your models here.
class ReportIncident(models.Model):
    place = models.CharField(max_length=50, blank=False)

    personalNumber = models.CharField(blank=False, max_length=12)
    time = models.DateField(blank=False, null=True, default=None)

    description = models.TextField(max_length=500, blank=False)
    action = models.TextField(max_length=500, blank=True)

    image = models.ImageField(upload_to='images/', blank=True)

