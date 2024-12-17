from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['id']
        
        labels = {
            'name' : 'Product Name',
            'price' : 'Unit Price',
            'expiry_date' : 'Expiry Date'
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter the product name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Provide a detailed product description'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Enter product quantity'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter unit price'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
        error_messages = {
            'name' : {'required' : 'Product should have a valid name'},
            'price' : {'required' : 'Product must have price'},
        }

