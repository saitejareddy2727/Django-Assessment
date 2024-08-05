from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def posts_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})