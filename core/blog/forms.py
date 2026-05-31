from django import forms
from blog.models import category, Post

class Catform(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name',]

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']