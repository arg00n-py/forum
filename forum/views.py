from django.shortcuts import render

from board.models import Category, Post


def homepage(request):
    categories = Category.objects.filter(active=True)
    latest_posts = Post.objects.order_by('-date_created')

    return render(request,
                  "board/homepage.html",
                  {'categories': categories,
                   'latest_posts': latest_posts})
