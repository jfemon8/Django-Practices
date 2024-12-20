from django.contrib import admin
from .models import Categories
# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
