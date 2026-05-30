from django import forms
from blog.models import category

class Catform(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name',]
        