from pickletools import int4
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import Event, RequestEvent
from .forms import CreateUserForm, SearchMonthForm
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.core.mail import send_mail
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from config import settings

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
    if request.method == 'POST':
        
        email = request.user.email
        id = request.user.id
        name = request.user.username
        type = request.POST['type']
        theme = request.POST['theme']
        people = request.POST['number']
        date = request.POST['date']
        address = request.POST['address']
        package = request.POST.get("item-options", True)
        terms_and_conditions = bool(request.POST.get("terms_and_conditions"))
        send_mail("Contact Form", name + " has requested a " + type + " event with a " + theme + " theme! There will be " + people + " people and it will be on " + date + " at " + address + "!" + "Here's their email: " + email,settings.EMAIL_HOST_USER, ['jazzysfamilycreations@gmail.com'], fail_silently=False)
        form = RequestEvent(id,name, type, theme, people, date, address, package, terms_and_conditions)
        form.save()
    return render(request, "events.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')
 
def calendartView(request):
    form = SearchMonthForm()
    if request.method == "GET":
        form = SearchMonthForm(request.GET)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
        else:       
            year = datetime.now().year
            month = datetime.now().strftime('%B')
    events = Event.objects.all()
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    event_list = Event.objects.filter(
        select_date__year = year,
        select_date__month = month_number
    )


    
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
        "form": form,
        "event_list":event_list,
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
    fields = ['type', 'theme', 'people', 'location', 'select_date', 'client']
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


def packagePage(request):
    context = {}
    return render(request, "packages.html", context)

    