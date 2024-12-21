from django import forms
from .models import Task

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
        labels = {'is_completed':'Mark as Completed', }
        
        widgets = {'category':forms.CheckboxSelectMultiple(), }
        
