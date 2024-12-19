from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.


def categories(request):
    categories = models.Categories.objects.all().order_by('-id')
    return render(request, 'categories.html', {'categories':categories})

def add_category(request):
    if request.method == 'POST':
        form = forms.CategotyForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('categories') 
    else:
        form = forms.CategotyForm()
    return render(request, 'category_form.html', {'form': form})

def edit_category(request, id):
    category = models.Categories.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.CategotyForm(request.POST, instance=category)
        if form.is_valid():
            form.save()   
    else:
        form = forms.CategotyForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def delete_category(request, id):
    author = models.Categories.objects.get(pk=id).delete()
    return redirect('categories')
