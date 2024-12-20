from django.shortcuts import render
from . import forms

# Create your views here.

def geeksforgeeks(request):
    form = forms.gfgForm()
    return render(request, 'geeksforgeeks.html', {'form':form})

def ordinarycoders(request):
    form = forms.ocForm()
    return render(request, 'ordinarycoders.html', {'form':form})

