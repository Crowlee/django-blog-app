from django import forms
from .models import  import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        