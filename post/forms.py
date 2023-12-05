from .models import Comment, Post, Rule
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category', 'anonymous_nickname', 'images']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': False,'class': 'form-control'}),
        }




class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ['name', 'content',]