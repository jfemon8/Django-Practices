from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ordinarycoders, name='oc'),
    path('gfg/', views.geeksforgeeks, name='gfg'),
]