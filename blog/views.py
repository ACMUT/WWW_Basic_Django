from django.shortcuts import render

from blog.models import BlogPost


def get_posts(request):
    context = {'posts': BlogPost.objects.all()}
    return render(request, 'blog/index.html', context)
