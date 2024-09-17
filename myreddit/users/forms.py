from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Last Name'}),
        }
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Username / Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Password'}))
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
    
class PasswordChangeUserForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Old Password'}))
    new_password1  = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'New Password'}))
    new_password2  = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = get_user_model()
        field = ['old_password', 'new_password1', 'new_password2']

class PasswordResetUserForm(PasswordResetForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Email'}))

class PasswordResetConfirmUserForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-3 py-2', 'placeholder': 'Confirm Password'}))
        
        
