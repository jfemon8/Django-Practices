from django import forms
from .models import Categories

class CategotyForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
        
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': 'Enter category name . . .'}),
            }