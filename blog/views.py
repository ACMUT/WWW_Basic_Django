from django.shortcuts import render

from blog.models import BlogPost


def get_posts(request):
    author = request.GET.get('author')
    if author:
        context = {'posts': BlogPost.objects.filter(author=author)}
    else:
        context = {'posts': BlogPost.objects.all()}
    return render(request, 'blog/index.html', context)
