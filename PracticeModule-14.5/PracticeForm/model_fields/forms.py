from django import forms
from .models import Medium

class ModelForm(forms.ModelForm):
    class Meta:
        model = Medium
        fields = '__all__'
        
