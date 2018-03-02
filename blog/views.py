from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import BlogPost


def get_posts(request):
    author = request.GET.get('author')
    if author:
        context = {'posts': BlogPost.objects.filter(author=author)}
    else:
        context = {'posts': BlogPost.objects.all()}
    return render(request, 'blog/posts.html', context)

def new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        blogPost = BlogPost(title=title, content=content)
        blogPost.save()
        return HttpResponseRedirect('/posts')

    return render(request, 'blog/form.html')
