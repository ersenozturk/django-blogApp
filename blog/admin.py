from atexit import register
from xml.etree.ElementTree import Comment
from django.contrib import admin

from blog.models import Category, PostComment, PostLike, PostView, Posts
from users.models import Profile

admin.site.register(Posts)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(PostComment)
admin.site.register(PostView)
admin.site.register(PostLike)

