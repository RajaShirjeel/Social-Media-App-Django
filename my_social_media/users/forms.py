from typing import Any
from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-inputs', 'id': 'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-inputs', 'id': 'confirm_password'}))


    class Meta: 
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-inputs"}),
            'email': forms.TextInput(attrs={"class": "form-inputs"})
        }
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'password': 'Password',
            'confirm_password': 'Confirm Password'
        }


    def clean(self):
        cleaned_data =  super().clean()
        password = cleaned_data.get('password')
        confirm_pass = cleaned_data.get('confirm_password')

        if password != confirm_pass:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data

