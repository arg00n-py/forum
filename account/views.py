from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserRegistrationForm, UserProfileEditForm, UserLoginForm


def homepage(request):
    # homepage for anonymous users
    return render(request, "board/homepage.html")


@login_required(login_url='account:login')
def dashboard(request):
    # user dashboard
    return render(request, 'account/dashboard.html')


def user_login(request):
    # user login
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect("account:dashboard")
                else:
                    return HttpResponse("User Disabled")

            else:
                return HttpResponse("Invalid login details")

    else:
        form = UserLoginForm()

    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    # user logout
    logout(request)
    return redirect("account:login")
