from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(requests):
    if requests.method == 'POST':
        form = UserRegisterForm(requests.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(requests,f'Account created for {username} was successful. You can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(requests,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

