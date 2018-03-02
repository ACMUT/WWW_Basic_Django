from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return "Tag:" + self.title


class BlogPost(models.Model):
    author = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=255, null=False, unique=True)
    content = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.author + ":" + self.title


class Comment(models.Model):
    content = models.TextField(max_length=4000)
    blogPost = models.ForeignKey(BlogPost,
                                 on_delete=models.CASCADE,
                                 related_name="comments")


