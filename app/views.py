from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


from .models import *
from .forms import CreateUserForm

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

