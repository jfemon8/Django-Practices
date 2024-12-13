from django.urls import path
from . import views

urlpatterns = [
    path('earthly/', views.earthly),
    path('geeksforgeeks/', views.geeksforgeeks),
    path('', views.test),
]