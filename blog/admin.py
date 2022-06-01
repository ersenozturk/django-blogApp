from atexit import register
from django.contrib import admin

from blog.models import Posts

admin.site.register(Posts)