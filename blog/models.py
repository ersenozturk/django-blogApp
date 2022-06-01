from enum import auto
from django.db import models
from django.contrib.auth.models import User



class Posts(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="media/", null = True, blank = True)

    # CATEGORIES = (
    #     ("FS", "Full Stack"),
    #     ("FE", "Front End"),
    #     ("Be", "Back End"),
    # )

    STATUS = (
        ("DR", "Draft"),
        ("PB", "Publish"),
        
    )

    # categories = models.CharField(max_length=50, choices=CATEGORIES)
    status = models.CharField(max_length=50, choices=STATUS)
    publish_date = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True )
    slug = models.SlugField(verbose_name="slug", allow_unicode=True, unique=True, max_length=100, default=title)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    
    