
from django import forms
from django.forms import ModelForm
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class ToDoForm(forms.Form):
#         date = forms.DateField(
#             widget=DatePickerInput(
#                 options={
#                     "format": "mm/dd/yyyy",
#                     "autoclose": True
#                 }
#             )
#         )


class SearchMonthForm(forms.Form):
    year = forms.IntegerField(required=True)
    month = forms.CharField(required=True)