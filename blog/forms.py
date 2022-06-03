from django import forms
from .models import Posts, PostComment, PostLike
# from django.contrib.auth.models import User 
# from django.contrib.auth.forms import UserCreationForm


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