from django.urls import path
from .views import user_login, user_logout, user_register, user_home

urlpatterns = [
    # path('', user_home, name='home'),
    path('register', user_register, name='register'),
    path('logout', user_logout, name='logout'),
    path('login', user_login, name='login'),
]
