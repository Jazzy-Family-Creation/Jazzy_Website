from django.dispatch import receiver
from config import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import *
from .forms import CreateUserForm
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.core.mail import send_mail


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
        name = request.user.username
        type = request.POST['type']
        theme = request.POST['theme']
        people = request.POST['number']
        date = request.POST['date']
        address = request.POST['address']
        send_mail("Contact Form", name + " has requested a " + type + " event with a " + theme + " theme! There will be " + people + " people and it will be on " + date + " at " + address + "!",settings.EMAIL_HOST_USER, ['rbennett22@basecampcodingacademy.org'], fail_silently=False)
    return render(request, "events.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')
 
def calendartView(request):
    events = Event.objects.all()
    context = {
        'events': events
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
