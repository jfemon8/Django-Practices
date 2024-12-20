from django.contrib import admin
from .models import Album

# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'release_date')
    search_fields = ('album_name', 'release_date')
    
