from django.contrib import admin
from .models import Blogs

# Register your models here.

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'author__name')