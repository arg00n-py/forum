from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import UserProfile


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea)
    date_of_birth = forms.DateField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'date_of_birth',
                  'bio', 'email', 'password1', 'password2')


class UserProfileEditForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('bio', 'date_of_birth')


class PasswordChangeForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)
    new_password_again = forms.CharField(widget=forms.PasswordInput)