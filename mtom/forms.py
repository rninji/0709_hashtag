from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['name','image','price','shop','type']

class TagForm(forms.ModelForm):
    class Meta:
        model=Tag
        fields=['name']