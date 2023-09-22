from django.shortcuts import render
from .models import Provider, Product
from django.shortcuts import render, redirect, get_object_or_404
from cart.forms import AddProductForm


def product_list(request, product_provider_name=None):
    products = Product.objects.all()
    provider = None
    providers = Provider.objects.all()
    sort = request.GET.get('sort')

    if product_provider_name:
        provider = get_object_or_404(Provider, name=product_provider_name)
        products = products.filter(provider=provider)
    return render(request,
                  'product/list_products.html',
                  {'provider': provider,
                   'providers': providers,
                   'products': products})

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request,
                  'product/product_details.html',
                  {'product': product, 'add_to_cart_form': AddProductForm()})

def about_company(request):
    return render(request, 'information/about_company.html')

def faq(request):
    return render(request, 'information/faq.html')

def news(request):
    return render(request, 'information/news.html')

def privacy_policy(request):
    return render(request, 'information/privacy_policy.html')

def home(request):
    return render(request, 'product/home.html')