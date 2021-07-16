from django.urls import path
from . import views


app_name = 'account'


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]