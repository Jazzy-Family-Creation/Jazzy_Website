from django.db import models


class Event(models.Model):
    type = models.CharField(max_length=200, null=True)
    theme = models.CharField(max_length=200, null=True)
    people = models.IntegerField()
    location = models.CharField(max_length=200, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()