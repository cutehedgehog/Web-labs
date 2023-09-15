from django.db import models
from django.urls import reverse
        
class Provider(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"
       
    def get_absolute_url(self):
        return reverse('shop:list_products_by_provider', args=[self.name])
        
class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_code = models.CharField(max_length=20)
    provider = models.ForeignKey(
        Provider, related_name='products', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_details', args=[str(self.id)])

