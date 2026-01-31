from django import forms

from .models import LostFoundItem


class LostFoundItemForm(forms.ModelForm):
    class Meta:
        model = LostFoundItem
        fields = ['title', 'status', 'location', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
        }
