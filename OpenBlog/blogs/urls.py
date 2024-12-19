from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='home'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('edit_blog/<int:id>', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:id>', views.delete_blog, name='delete_blog'),
]
