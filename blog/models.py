from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="media/")

    CATEGORIES = (
        ("FS", "Full Stack"),
        ("FE", "Front End"),
        ("Be", "Back End"),
    )

    STATUS = (
        ("FS", "Full Stack"),
        ("FE", "Front End"),
        ("Be", "Back End"),
    )

    categories = models.CharField(max_length=50, choices=CATEGORIES)
    status = models.CharField(max_length=50, choices=STATUS)


    def __str__(self):
        return self.title
