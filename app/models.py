from django.db import models
from datetime import datetime



class Event(models.Model):
    PACKAGES = (
        ("Basic Deposit", "Base"),
        ("Premium Deposit", "Premium"),
        ("Gold Deposit", "Gold")
    )
    type = models.CharField(max_length=200, null=True)
    theme = models.CharField(max_length=200, null=True)
    people = models.IntegerField(null=True)
    location = models.CharField(max_length=200, null=True)
    select_date = models.DateField(auto_now=False)
    package = models.CharField(max_length=200, null=True,choices=PACKAGES)
    client = models.CharField(max_length=200, null=True)
        
class RequestEvent(models.Model):
    PACKAGES = (
        ("Basic Deposit", "Base"),
        ("Premium Deposit", "Premium"),
        ("Gold Deposit", "Gold")
    )
    name = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    theme = models.CharField(max_length=200, null=True)
    people = models.IntegerField(null=True)
    request_date = models.DateField()
    address = models.CharField(max_length=200, null=True)
    package = models.CharField(max_length=200, null=True,choices=PACKAGES)
    terms_and_conditions = models.BooleanField(null=True)




