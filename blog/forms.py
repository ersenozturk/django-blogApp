from django import forms
from .models import Category, Posts, PostComment, PostView, PostLike
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'content',
            'image',
            'bg_image_url',
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