from django import template
from django.template.loader import get_template

from board.models import Category, Post
from account.models import User
# from account.views import user_login

register = template.Library()


@register.inclusion_tag('inclusion_templates/category_list.html')
def show_category_list():
    categories = Category.objects.filter(active=True)

    return({'category_list': categories})


# @register.inclusion_tag('inclusion_templates/conditional_login_form.html')
# def conditional_login_form(request):
#     # pass to account.views.user_login
#     context = user_login(request)

#     return(context)


@register.inclusion_tag('inclusion_templates/forum_stats.html')
def forum_stats():
    categories = Category.objects.filter(active=True)
    posts = Post.objects.filter(approved=True)
    users = User.objects.filter(is_active=True)

    return ({'categories': categories,
             'posts': posts,
             'users': users})

@register.inclusion_tag('inclusion_templates/recent_posts.html')
def recent_posts():
    all_posts = Post.objects.filter(approved=True)

    latest_posts = all_posts.order_by('-date_created')[:5]

    return ({'latest_posts': latest_posts})
