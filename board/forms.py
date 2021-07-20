from django import forms
from .models import Category, Post


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['admin', 'title', 'description']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'category', 'content']