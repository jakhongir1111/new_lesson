from django.db.models import Q
from django.shortcuts import render

from apps.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def detail(request, slug):
    post = Post.objects.filter(slug=slug).first()
    author = post.author
    author_posts = Post.objects.filter(~Q(slug=slug), author=author)
    # eye = Post.objects.filter(slug=slug).first()
    # Post.objects.filter(slug=slug).update(views=eye.views + 1)
    post.views += 1
    post.save()
    return render(request, 'blog_detail.html', {'post': post, 'author_posts': author_posts})
