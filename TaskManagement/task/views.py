from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.

def view_task(request):
    tasks = models.Task.objects.all().order_by('-id')
    return render(request, 'view_task.html', {'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_task')
    else:
        form = forms.CategoryForm()
    return render(request, 'task_details.html', {'form':form})

def edit_task(request, id):
    task = models.Task.objects.get(pk=id) 
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_task')
    else:
        form = forms.CategoryForm(instance=task)
    return render(request, 'task_details.html', {'form':form})

def delete_task(request, id):
    task = models.Task.objects.get(pk=id).delete()
    return redirect('view_task')

def complete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('view_task')