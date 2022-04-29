from django.contrib import admin
from app.models import Event, RequestEvent

# Register your models here.
admin.site.register(Event)
admin.site.register(RequestEvent)
