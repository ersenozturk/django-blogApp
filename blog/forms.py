from django import forms

from blog.models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"
        # exclude = ("slug",)