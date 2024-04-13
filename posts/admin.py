from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_publicacao', 'tema']
    list_filter = ['autor', 'tema']
    search_fields = ['titulo', 'tema']

admin.site.register(Post, PostAdmin)
