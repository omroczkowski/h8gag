from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'field',
        'placeholder': 'Enter Password'
        }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'field',
        'placeholder': 'Repeat Email'
        }))
    class Meta():
        model = User
        fields = ('username','email','password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'field',
                'placeholder': 'Enter Username'
                }),
            'email': forms.EmailInput(attrs={
                'class': 'field',
                'placeholder': 'Enter Email'
                })
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )