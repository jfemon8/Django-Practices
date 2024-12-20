from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddAlbum, name='add_album'),
    path('edit/<int:id>', views.EditAlbum, name='edit_album'),
]