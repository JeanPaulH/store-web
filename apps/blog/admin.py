from django.contrib import admin
from apps.blog.blog import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at')
    search_fields = ('title',)
    list_filter = ('published', 'created_at')
