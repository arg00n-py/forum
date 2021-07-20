from django.urls import path
from . import views


app_name = 'account'


urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('signup/', views.user_signup, name="signup"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('password_change/', views.password_change, name="password_change")
]