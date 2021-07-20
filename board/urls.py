from django.urls import path
from . import views

app_name = 'board'


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('add_category/', views.add_category, name="add_category")
]
