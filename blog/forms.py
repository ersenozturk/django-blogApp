from django import forms
<<<<<<< HEAD
from .models import Category, Posts, PostComment, PostLike
=======
from .models import Posts, PostComment, PostLike
# from django.contrib.auth.models import User 
# from django.contrib.auth.forms import UserCreationForm
>>>>>>> 53dccece7fc5de29e0235fa9c1b35687462d438f


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'content',
            'image',
            'status',
            'slug',
            'category',
        ]



class LikeForm(forms.ModelForm):
    class Meta:
        model = PostLike
        fields = [
            # 'user', 
            # 'posts'
            ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['content']