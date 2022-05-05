"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoconfig.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from app.models import *


urlpatterns = [
    path("register/", registerPage, name="register"),
    path('admin/', admin.site.urls),
    path('login/', loginPage, name="login"),
    path("", indexPage, name="index" ),
    path("events/", eventsPage, name="events"),
    path("logout/", logoutUser, name="logout"),
    path("calendar/", calendartView, name = "calendar"),
    path("packages/", packagePage, name = "packages"),
    # path("calendar/", calendartView, name = "calendar"),
    path("event_list/", EventList.as_view(), name="event_list"),
    path("event/<int:pk>", EventDetail.as_view(), name="event"),
    path("event-create", EventCreate.as_view(), name="event-create"),
    path("event-update/<int:pk>", EventUpdate.as_view(), name="event-update"),
    path("event-delete/<int:pk>", DeleteView.as_view(), name="event-delete"),
    path("requested-events", viewRequestedEvents, name="requested-events")
    
    ]
#<int:year>/<str:month>/