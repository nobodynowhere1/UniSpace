from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'description', 'price', 'status', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
        }
