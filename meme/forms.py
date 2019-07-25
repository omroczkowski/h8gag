from django import forms
from .models import Meme

class MemeForm(forms.ModelForm):
    class Meta():
        model = Meme
        fields = ('description','category','meme_img')
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'field',
                'placeholder': 'Enter Description'
                }),
            'category': forms.Select(choices=model.CATEGORY_CHOICES, attrs={
                'class': 'choice-control',
                'placeholder': 'Choose category',
            }),
            'meme_img': forms.FileInput(attrs={
                'class': 'upload-control',
                'placeholder': 'Choose file',
            })
        }