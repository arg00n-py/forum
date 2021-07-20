from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from account.models import UserProfile


class Category(models.Model):
    admin = models.ManyToManyField(UserProfile,
                                   limit_choices_to={'is_admin': True})
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:category_detail',
                       kwargs={'title': self.title})


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:post_detail',
                       kwargs={'category': self.category,
                               'id': self.id,
                               'title': self.title})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', 
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True,
                              related_name='replies')
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_created',]

    def __str__(self):
        return f'{self.user.username}\'s comment'