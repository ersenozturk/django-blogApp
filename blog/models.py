from django.db import models
from django.contrib.auth.models import User




class Category(models.Model): 
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name  



class Posts(models.Model):  

    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/%Y")

    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ("dft", "draft"),
        ("pbl", "publish"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    slug = models.SlugField(
        verbose_name='slug',
        allow_unicode=True,
        unique=True,
        max_length=255,
        default=title,
        help_text=(
            "The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/")
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title + " " + self.status

  
    

class PostComment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')

    def __str__(self):
        return self.user.username.title() + ' - ' + self.post.title





class PostView(models.Model):
    timestamp = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='views')
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='views')

    def __str__(self):
        return str(self.user) + ' - ' + self.posts.title




class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="likes")
    posts = models.ForeignKey(Posts, on_delete=models.SET_NULL, null=True, related_name="likes")

    def __str__(self):
        return self.user.username + ' - ' + self.posts.title

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['posts', 'user'], name="unique_like")
        ]
