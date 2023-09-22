from django import forms
from .models import Product, ProductCategory


class ProductForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=ProductCategory.objects.all())
    class Meta:
        model = Product
        fields = ['name', 'price', 'vendor_code', 'categories']