from django import forms
from .models import Authors

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'
        
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': 'Enter author name . . .'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter author phone number . . .'}),
            }
