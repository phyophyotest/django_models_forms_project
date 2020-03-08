# from django import forms
# from .models import Category

# class CategoryForm(forms.ModelForm):
#     name=forms.CharField(max_length=225)

# class Meta:
#     model=Category
#     field=['name']

from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    name=forms.CharField(max_length=255)

    class Meta:
        model=Category
        fields=['name']


