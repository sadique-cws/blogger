from django import forms
from .models import *


class InsertForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("author",)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__" 
        