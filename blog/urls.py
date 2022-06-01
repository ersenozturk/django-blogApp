# from django.urls import path

# from blog.views import post_list as home


from django.urls import path
from blog.views import createPost, post_list, post_detail


urlpatterns = [
    path('create_post', createPost , name='create'),
    path('list_post', post_list , name='list'),
    path('list_detail/<int:id>', post_detail , name='detail'),
    


]
