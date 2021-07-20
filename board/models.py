from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    admin = models.ManyToManyField(User)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
