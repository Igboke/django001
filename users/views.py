from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated was successful. You can now login!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form' : p_form
    }
    return render(request,'users/profile.html',context)

