from django.db import models


class BlogPost(models.Model):
    author = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=255, null=False, unique=True)
    content = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
