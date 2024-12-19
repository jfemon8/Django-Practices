from django.contrib import admin
from .models import Authors
# Register your models here.

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')