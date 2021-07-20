from django import forms
from .models import Category, Post, Comment


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['admin', 'title', 'description']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'category', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
        # widgets = {'content': forms.TextInput}