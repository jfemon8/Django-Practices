from django import forms
from .models import Blogs

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
        
        widgets = {
            'categories':forms.CheckboxSelectMultiple,
            'title': forms.TextInput(attrs={'placeholder': 'Enter blog title . . .'}),
            }
    
        
