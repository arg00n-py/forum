from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    search_fields = ['title', 'active']
    list_filter = ['active']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category', 'date_created',
                    'approved']
    search_fields = ['title', 'user', 'category']
    list_editable = ['approved']
    list_filter = ['approved']
