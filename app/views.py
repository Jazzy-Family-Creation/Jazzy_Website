
from sqlite3 import complete_statement
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import *
from .forms import CreateUserForm
from django.http.response import Http404, HttpResponseRedirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.

def registerPage (request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect("login")
    context = {"form": form}
    return render(request, "register.html", context)

def indexPage(request):
    context = {}
    return render(request, "index.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method== "POST":
            username =request.POST.get("username")
            password =request.POST.get("password")
            user =authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'User OR password is incorrect')
                return render(request, "login.html")
    context = {}
    return render(request, "login.html", context)

def eventsPage(request):
    context = {}
    return render(request, "events.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')
 
def calendartView(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    events = Event.objects.all()
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    #create Calender
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M %p')
    context = {
        'events': events,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    }
    return render(request, "calendar.html", context)

class EventList(ListView,LoginRequiredMixin):
    model=Event
    context_object_name = 'events'

    def get_context_data(self):
        context = super().get_context_data()
        context['events'] = context['events']
        context['count'] = context['events'].count()
        return context
    
    
class EventDetail(DetailView):
    model= Event
    context_object_name = 'event'

class EventCreate(CreateView):
    model = Event
    fields = ['type', 'theme', 'select_date', 'location', 'people']
    success_url = reverse_lazy('event_list')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(EventCreate, self).form_valid(form)

class EventUpdate(UpdateView):
    model = Event
    fields = ['type', 'theme', 'people', 'location', 'select_date']
    success_url = reverse_lazy('event_list')

class DeleteView(DeleteView):
    model = Event
    context_object_name = 'event'
    success_url = reverse_lazy('event_list')


