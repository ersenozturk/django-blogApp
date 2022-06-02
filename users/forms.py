from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Profile

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')



#!

class ProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bg_image_url', 'bio']



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']