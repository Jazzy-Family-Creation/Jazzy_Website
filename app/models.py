from django.db import models
from datetime import datetime



class Event(models.Model):
    type = models.CharField(max_length=200, null=True)
    theme = models.CharField(max_length=200, null=True)
    people = models.IntegerField(null=True)
    location = models.CharField(max_length=200, null=True)
    select_date = models.DateField(auto_now=False)
    client = models.CharField(max_length=200, null=True)
        
    