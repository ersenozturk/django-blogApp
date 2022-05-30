from django.urls import path
from .views import deneme

urlpatterns = [
    path('', deneme, name='deneme')
]
