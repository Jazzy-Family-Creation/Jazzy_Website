from django.db import models
from datetime import datetime


class Event(models.Model):
    type = models.CharField(max_length=200, null=True)
    theme = models.CharField(max_length=200, null=True)
    people = models.IntegerField()
    location = models.CharField(max_length=200, null=True)
    select_date = models.DateTimeField(auto_now=False)