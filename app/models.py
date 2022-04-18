from django.db import models
from datetime import datetime

# class Event(models.Model):
#     type = models.CharField(max_length=200, null=True)
#     theme = models.CharField(max_length=200, null=True)
#     people = models.IntegerField()
#     location = models.CharField(max_length=200, null=True)
#     select_date = models.DateField(auto_now=False)
#     client = models.CharField(max_length=200, null=True)
    
class Venue(models.Model):
    name = models.CharField("Venue Name", max_length=200),
    address = models.CharField(max_length=300),
    zip_code = models.CharField('Zip Code', max_length=15),
    phone = models.CharField('Contact Phone', max_length=25),
    web = models.URLField('Website Address'),
    email_address = models.EmailField('Email Address', max_length=120),
    
    
    def __str__(self):
        return self.name
   
   

   
class Event(models.Model):
    type = models.CharField('Type of Event', max_length=200, null = True),
    theme = models.CharField(max_length=200, null=True),
    select_date = models.DateTimeField('Event Date'),
    venue = models.ForeignKey(Venue, blank = True, null=True, on_delete=models.CASCADE)
    people = models.IntegerField(null=True)
    client = models.CharField('Client Name', max_length=400),

    
    def __str__(self):
        return self.client
    
class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email', max_length=120)
    number = models.CharField(max_length=30)
    events = models.ForeignKey(Event, blank = True, null = True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
 
    
    
    
    