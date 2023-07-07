from django.db.models import Q
from django.shortcuts import render

from apps.models import Post, Comment


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def detail(request, slug):
    post = Post.objects.filter(slug=slug).first()
    if request.POST:
        data = request.POST
        name = data.get('Name')
        email = data.get('Email')
        text = data.get('message')
        Comment.objects.create(name=name, email=email, text=text, post=post)

    author = post.author
    author_posts = Post.objects.filter(~Q(slug=slug), author=author)
    post.views += 1
    post.save()
    return render(request, 'blog_detail.html', {'post': post, 'author_posts': author_posts})
