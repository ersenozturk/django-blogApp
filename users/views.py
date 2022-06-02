from pyexpat.errors import messages
from django.shortcuts import render, redirect

from blog.models import Posts
from .forms import ProfileForm, RegisterForm
from .forms import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def user_register(request):  # ok

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def user_logout(request):
    messages.success(request, 'You succesfully logged out')
    logout(request)
    return redirect('home')


def user_login(request):
    
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    
    return render(request, 'users/login.html', {'form':form})




def user_profile(request):  # ok

    if not request.user.is_authenticated:
        return redirect('login')

    post = Posts.objects.filter(user=request.user.id)
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    context = {
        'post': post,
        'profile': profile,
    }

    return render(request, 'users/profile.html', context)




def profileadd(request):  # ok

    if not request.user.is_authenticated:
        return redirect('login')

    form = ProfileForm()

    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)

        form = ProfileForm(request.POST, request.FILES, instance=user)

        # id otomatik olarak buradan yüklenir
        # Return an object without saving to the DB
        # obj = form.save(commit=False)
        # obj.user = User.objects.get(pk=request.user.id)

        if form.is_valid():

            form.save()
            messages.success(
                request, f'Your account has been created. You can log in now!')
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'users/profileadd.html', context)


def profileupdate(request):  # ok
    if not request.user.is_authenticated:
        return redirect('login')

    user = Profile.objects.get(user=request.user.id)
    form = ProfileForm(instance=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been created. You can log in now!')
            return redirect('profile')

    context = {
        'form': form,
    }
    return render(request, 'users/profileupdate.html', context)