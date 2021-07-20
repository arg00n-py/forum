from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm, CommentForm,  PostForm
from .models import Category, Post, Comment


# def homepage(request):
#     categories = Category.objects.filter(active=True)
#     latest_posts = Post.objects.order_by('-date_created')

#     return render(request,
#                   "board/homepage.html",
#                   {'categories': categories,
#                    'latest_posts': latest_posts})


def category_list(request):
    categories = Category.objects.filter(active=True)

    return render(request,
                  'board/category_list.html',
                  {'categories': categories})


def category_detail(request, title):
    category = Category.objects.get(title=title)
    posts = category.post_set.filter(approved=True)

    return render(request,
                  'board/category_detail.html',
                  {'posts': posts,
                   'category': category})


def post_detail(request, category, id, title):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.all().filter(active=True, post=post, parent__isnull=True)

    new_comment = None

    if not post.approved:
        messages.error(request, "Post not found")
        return redirect('board:homepage')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            parent_obj = None

            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None

            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)

                if parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.parent = parent_obj

            new_comment = comment_form.save(commit=False)

            new_comment.post = post
            new_comment.user = request.user

            new_comment.save()

            messages.success(request, 'Comment added successfully')
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    return render(request,
                  'board/post_detail.html',
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form})


@login_required()
def add_category(request):

    if not request.user.userprofile.is_admin:
        messages.error(request, "Only admins can add categories.")
        return redirect('board:homepage')

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been added.')
            return redirect('board:homepage')

    else:
        form = CategoryForm()

    return render(request, 'board/add_category.html', {'form': form})


@login_required()
def add_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            form.save()

            post_title = form.cleaned_data['title']

            messages.success(request, f"'{post_title}' posted successfully.")

            return redirect('board:homepage')

    else:
        form = PostForm()

    return render(request, 'board/add_post.html', {'form': form})


@login_required()
def add_comment(request):
    pass


@login_required()
def add_reply(request):
    pass
