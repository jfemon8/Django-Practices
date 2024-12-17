from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_product/', views.productForm, name='new_product'),
    path('delete/<int:id>', views.deleteProduct, name='delete'),
    path('edit/<int:id>', views.editProduct, name='edit')
]
