from django.shortcuts import get_object_or_404, render

from .models import Post


def index(request):
    return render(request, "app/index.html")


def blog(request):
    posts = Post.objects.filter(status="published").order_by("-created_at")
    return render(request, "app/blog.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "app/post_detail.html", {"post": post})
