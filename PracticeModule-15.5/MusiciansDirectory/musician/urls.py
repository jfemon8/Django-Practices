from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_musician/', views.AddMusician, name='add_musician'),
    path('edit_musician/<int:id>', views.EditMusician, name='edit_musician'),
    path('delete_musician/<int:id>', views.DeleteMusician, name='delete_musician'),
]