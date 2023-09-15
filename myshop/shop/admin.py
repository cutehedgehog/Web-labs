from django.contrib import admin
from .models import Provider, Product

class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    
admin.site.register(Provider, ProviderAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'vendor_code']
    list_editable = ['price']
    
admin.site.register(Product, ProductAdmin)
