from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import  UserForm
from django.contrib.auth.forms import AuthenticationForm


def user_homee(request):
    return render(request, 'users/homee.html')

def user_logout(request):
    messages.success(request, 'You succesfully logged out')
    logout(request)
    return redirect('homee')

def  user_register(request):
    
    form_user = UserForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)

        if form_user.is_valid():
            user = form_user.save()

            login(request, user)
            messages.success(request, 'register done!')
            return redirect ('homee')

    context = {
        'form_user' : form_user,
    }

    return render(request, 'users/register.html', context)


def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('homee')
    
    return render(request, 'users/login.html', {'form':form})