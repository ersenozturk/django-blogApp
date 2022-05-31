from django.urls import path

from blog.views import home


urlpatterns = [
    path('', home, name='home'),
    path('logout', home, name='home'),

]
