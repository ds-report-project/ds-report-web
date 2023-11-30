from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category', 'anonymous_nickname', 'image']  
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True,'class': 'form-control'}),
        }

