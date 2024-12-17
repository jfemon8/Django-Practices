from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.

def home(request):
    products = models.Product.objects.all()
    return render(request, 'home.html', {'products' : products})


def productForm(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.ProductForm()  
    else:
        form = forms.ProductForm()  
    return render(request, 'product_form.html', {'form': form})

def deleteProduct(request, id):
    product = models.Product.objects.get(pk=id).delete()
    return redirect("home")

def editProduct(request, id):
    product = models.Product.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()  
    else:
        form = forms.ProductForm(instance=product)  
    return render(request, 'product_form.html', {'form': form})

    