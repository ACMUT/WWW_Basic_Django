from django.contrib import admin

from blog.models import BlogPost, Tag, Comment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)