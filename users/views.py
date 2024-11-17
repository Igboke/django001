from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(requests):
    form = UserCreationForm()
    return render(requests,'users/register.html',{'form':form})

