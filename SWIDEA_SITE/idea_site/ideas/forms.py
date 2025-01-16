from django import forms
from .models import Idea  # 아이디어 모델

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'category'] 
