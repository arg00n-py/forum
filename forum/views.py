from django.shortcuts import render

from board.models import Category, Post


def homepage(request):
    categories = Category.objects.filter(active=True)

    all_posts = Post.objects.filter(approved=True)

    latest_posts = all_posts.order_by('-date_created')

    context = {'categories': categories,
                'all_posts': all_posts.order_by('?'),
                'latest_posts': latest_posts,
                'section': 'homepage'}

    if request.user.is_authenticated:
        user_posts = all_posts.filter(user=request.user)

        context['user_posts'] = user_posts


    return render(request,
                  "board/homepage.html",
                  context)
