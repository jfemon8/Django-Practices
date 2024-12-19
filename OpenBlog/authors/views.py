from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.


def authors(request):
    authors = models.Authors.objects.all().order_by('-id')
    return render(request, 'authors.html', {'authors':authors})

def add_author(request):
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('authors') 
    else:
        form = forms.AuthorForm()
    return render(request, 'author_form.html', {'form': form})

def edit_author(request, id):
    author = models.Authors.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()   
    else:
        form = forms.AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form})

def delete_author(request, id):
    author = models.Authors.objects.get(pk=id).delete()
    return redirect('authors')
