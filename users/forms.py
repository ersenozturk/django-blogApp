from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ModelForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']