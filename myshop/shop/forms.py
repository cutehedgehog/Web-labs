from django import forms
from .models import Product, ProductCategory, Provider


class ProductForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=ProductCategory.objects.all())
    class Meta:
        model = Product
        fields = ['name', 'price', 'vendor_code', 'categories']


# class ProviderForm(forms.Form):
#     provider = forms.ChoiceField()
#     def __init__(self, *args, **kwargs):
#         choices = kwargs.pop('choices', [])
#         super(ProviderForm, self).__init__(*args, **kwargs)
#         self.fields['provider'].choices = choices
