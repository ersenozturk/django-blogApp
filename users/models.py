from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):  # ok
    image = models.ImageField(upload_to="profiles/%Y", default="default.jpg")
    bg_image_url = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        help_text="Zorunlu değil, Eğer resim kaybolursa arkaplan fotoğrafı olarak bu url adresindeki fotoğraf kalır"
    )
    bio = models.TextField(max_length=5000, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username