from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ("draft", "Draft"),
        ("published", "Published")
    ], default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
