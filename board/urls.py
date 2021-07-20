from django.urls import path
from . import views

app_name = 'board'


urlpatterns = [
    # path('', views.homepage, name="homepage"),
    path('add_category/', views.add_category, name="add_category"),
    path('add_post/', views.add_post, name="add_post"),
    path('categories/', views.category_list, name="category_list"),
    path('<str:title>/', views.category_detail, name="category_detail"),
    path('<str:category>/<int:id>/<str:title>/', views.post_detail, name="post_detail"),
]
