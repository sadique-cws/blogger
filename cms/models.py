from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    cat_title = models.CharField(max_length=200)
    cat_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cat_title
    


class Post(models.Model):
    title = models.CharField(max_length=200,help_text="enter your post title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dateofPub = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="post/")

    def __str__(self):
        return self.title