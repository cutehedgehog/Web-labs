from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('about_company/', views.about_company, name='about'),
    path('faq/', views.faq, name='faq'),
    path('news/', views.news, name='news'),
    path('list_products/', views.product_list, name='list_products'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('list_products/<int:id>', views.product_details, name='product_details'),
    path('list_products/<str:product_provider_name>/', views.product_list,
         name='list_products_by_provider'
         ),

]
