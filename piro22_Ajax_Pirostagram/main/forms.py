from django import forms
from django.forms.widgets import TextInput
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border-radius: 15px;'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'border-radius: 15px;'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border-radius: 15px;',
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'  # 전체 필드