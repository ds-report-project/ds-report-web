from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category', 'anonymous_nickname', 'images']  
        widgets = {
            'images': forms.ClearableFileInput(attrs={'multiple': True,'class': 'form-control'}),
        }

