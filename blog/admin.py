from django.contrib import admin

from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author',)


admin.site.register(BlogPost, BlogPostAdmin)
