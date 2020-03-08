from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    name=forms.CharField(max_length=255)
    price=forms.IntegerField()
    image=forms.ImageField()
    
    class Meta:
        model=Product
        fields=['name','price','image']
