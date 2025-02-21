from django.contrib import admin
from django.urls import include, path

from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("__reload__/", include("django_browser_reload.urls")),
]
