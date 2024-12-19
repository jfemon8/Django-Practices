from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.

def blogs(request):
    blogs = models.Blogs.objects.all().order_by('-id')
    return render(request, 'blogs.html', {'blogs':blogs})

def add_blog(request):
    if request.method == 'POST':
        form = forms.BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('home') 
    else:
        form = forms.BlogForm()
    return render(request, 'blog_form.html', {'form': form})

def edit_blog(request, id):
    blog = models.Blogs.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()   
    else:
        form = forms.BlogForm(instance=blog)
    return render(request, 'blog_form.html', {'form': form})

def delete_blog(request, id):
    blog = models.Blogs.objects.get(pk=id).delete()
    return redirect('home')