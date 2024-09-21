from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Comment, Group, Post


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=200)

    class Meta:
        model = Comment
        fields = ['text']
        
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control my-3 py-2 w-75', 'placeholder': 'Text'})
        }
        
class AddPostForm(forms.ModelForm):
    text = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control my-3 py-2 w-75', 'placeholder': 'Title'}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-3 py-2 w-75', 'placeholder': 'Tags'}))
    url = forms.ImageField(label='Image', required=False)
    group = forms.ModelChoiceField(queryset=Group.objects.none(), empty_label='None Group')

    class Meta:
        model = Post
        fields = ['text', 'tags', 'url', 'group']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user is not None:
            self.fields['group'].queryset = Group.objects.filter(admin=user)   
class AddGroupForm(forms.ModelForm):
    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control my-3 py-2 w-75', 'placeholder': 'Group Name'}))
    description = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control my-3 py-2 w-75', 'placeholder': 'Description'}))
    photo = forms.ImageField()
    
    class Meta:
        model = Group
        fields = ['title', 'description', 'photo']