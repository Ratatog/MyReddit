from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    text = forms.TextInput()

    class Meta:
        model = Comment
        fields = ['text']
        
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control my-3 py-2 w-75', 'placeholder': 'Text'})
        }
        
class AddPostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-3 py-2 w-75', 'placeholder': 'Title'}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-3 py-2 w-75', 'placeholder': 'Tags'}))
    img = forms.ImageField(label='Image')

    class Meta:
        model = Post
        fields = ['text', 'tags', 'img']