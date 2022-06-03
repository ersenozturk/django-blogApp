from django.urls import path
from blog.views import post_create, post_detail, post_update, about, post_delete


urlpatterns = [
    path('post_create/', post_create , name='create'),
    path('post_detail/<str:slug>', post_detail , name='detail'),
    path('post_update/<int:id>', post_update , name='update'),
    path('about/', about, name='about'),
    path('post_delete/<int:id>', post_delete, name='delete'),
]
