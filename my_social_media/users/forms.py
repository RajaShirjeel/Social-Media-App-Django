from typing import Any
from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-inputs', 'id': 'password', 'placeholder': 'Your password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-inputs', 'id': 'confirm_password', 'placeholder': 'Confirm password'}))


    class Meta: 
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={"placeholder": 'John Doe', "class": "form-inputs"}),
            'email': forms.TextInput(attrs={"placeholder": 'JohnDoe@gmail.com', "class": "form-inputs"})
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'confirm_password': 'Confirm Password'
        }


    def clean(self):
        cleaned_data =  super().clean()
        password = cleaned_data.get('password')
        confirm_pass = cleaned_data.get('confirm_password')

        if password and confirm_pass and password != confirm_pass:
            self.add_error('confirm_password',"Passwords do not match!")
        
        return cleaned_data


class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-inputs', 'id': 'password', 'placeholder': 'Your password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-inputs', 'id': 'email', 'placeholder': 'JohnDoe@gmail.com'}))
    