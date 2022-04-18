from django.contrib import admin
from app.models import Event, Venue, Users

# Register your models here.
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Users)
