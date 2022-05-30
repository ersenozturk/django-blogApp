from django.urls import path
from .views import user_login, user_register, user_logout, user_homee

urlpatterns = [
    path('', user_homee, name='homee'),
    path('register', user_register, name='register'),
    path('logout', user_logout, name='logout'),
    path('login', user_login, name='login'),
]
