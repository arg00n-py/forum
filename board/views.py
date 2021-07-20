from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm,  PostForm


def homepage(request):
    # homepage for users
    return render(request, "board/homepage.html")


@login_required()
def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been added.')
            return redirect('account:dashboard')

    else:
        form = CategoryForm()

    return render(request, 'board/add_category.html', {'form': form})