from django import forms
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
    img = forms.ImageField(label='Image')
    # group = forms.ChoiceField(choices=)

    class Meta:
        model = Post
        fields = ['text', 'tags', 'img', 'group']
        
class AddGroupForm(forms.ModelForm):
    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control my-3 py-2 w-75', 'placeholder': 'Group Name'}))
    description = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control my-3 py-2 w-75', 'placeholder': 'Description'}))
    photo = forms.ImageField()
    
    class Meta:
        model = Group
        fields = ['title', 'description', 'photo']