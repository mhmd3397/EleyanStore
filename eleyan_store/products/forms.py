from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image',
                  'category', 'features', 'hide_product', 'hide_quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'features': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'hide_product': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'hide_quantity': forms.CheckboxInput(attrs={'class': 'form-check'}),
        }
