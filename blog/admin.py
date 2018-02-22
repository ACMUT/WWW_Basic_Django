from django.contrib import admin

from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author',)


admin.site.register(Blog, BlogAdmin)
