from django.contrib import auth
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserRegistrationForm, UserProfileEditForm, UserLoginForm,\
    PasswordChangeForm
from .models import UserProfile


@login_required()
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
                    messages.success(request, "Login Successful")
                    return redirect("homepage")
                else:
                    # return HttpResponse("User Disabled")
                    messages.error(request, "Account has been disabled.")
                    return redirect("acccount:login")

            else:
                # return HttpResponse("Invalid login details")
                messages.error(request, "Invalid login credentials.")
                return redirect('account:login')

    else:
        form = UserLoginForm()

    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    # user logout
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect("account:login")


def user_signup(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            cd = form.cleaned_data

            date_of_birth = cd['date_of_birth']
            bio = cd['bio']

            username = cd['username']
            password = cd['password1']

            user = authenticate(username=username, password=password)

            user.userprofile.bio = bio
            user.userprofile.date_of_birth = date_of_birth

            login(request, user)

            messages.success(request, "Account has been created successfully")

            return redirect("account:dashboard")

    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html', {'form': form})


@login_required()
def edit_profile(request):
    try:
        userprofile = request.user.userprofile

    except UserProfile.DoesNotExist:
        userprofile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfileEditForm(data=request.POST, instance=userprofile)

        if form.is_valid():

            form.save()

            messages.success(request, "Your Profile has been updated.")

            return redirect("account:dashboard")
    else:
        form = UserProfileEditForm()

    return render(request, 'account/edit_profile.html', {'form': form})


@login_required()
def password_change(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            password1 = cd['new_password']
            password2 = cd['new_password_again']

            if password1 == password2:
                user = User.objects.get(username=request.user.username)
                user.set_password(password2)
                user.save()

                n_user = authenticate(
                    username=request.user.username, password=password2)

                login(request, n_user)

                messages.success(request, "Password updated successfully")

                return redirect('account:dashboard')

            else:
                # return HttpResponse('Passwords don\'t match')
                messages.error(request, "Passwords do not match")
                return redirect('account:password_change')

    else:
        form = PasswordChangeForm()

    return render(request, 'account/password_change.html', {'form': form})
