from django.shortcuts import render
from . import forms

# Create your views here.

def medium(request):
    form = forms.ModelForm()
    return render(request, 'medium.html', {'form':form})

