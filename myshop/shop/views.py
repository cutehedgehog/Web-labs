from django.shortcuts import render
from .models import Provider, Product, ProductCategory
from django.shortcuts import render, redirect, get_object_or_404
from cart.forms import AddProductForm
from login.models import MyUser
from .forms import ProductForm
from django.views.decorators.http import require_POST


def product_list(request, product_provider_name=None):
    provider = None
    user = None
    providers = Provider.objects.all()
    products = Product.objects.all()
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

def provider_details(request, name):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    provider = get_object_or_404(Provider, name=name)
    products = products.filter(provider=provider)
    return render(request,
                  'product/provider_details.html',
                  {'provider': provider,
                   'products': products,
                   'categories': categories})
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

@require_POST
def create_product(request, provider_name):
    provider = get_object_or_404(Provider, name=provider_name)
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.provider = provider
        product.save()
        form.save_m2m()
        return redirect('shop:list_products')
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/')

def edit_product(request, provider_name, id):
    product = get_object_or_404(Product, id=id)
    categories = ProductCategory.objects.all()
    provider = get_object_or_404(Provider, name=provider_name)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form_product = form.save(commit=False)
            form_product.provider = provider
            form_product.save()
            form.save_m2m()
            return redirect('shop:list_products')
    return render(request, 'product/edit_product.html', {'form': form, 'product': product, 'categories': categories})
# @require_POST
# def add_provider(request, user_email):
#     user = get_object_or_404(MyUser, email=user_email)
#     form = ProviderForm(request.POST)
#     if form.is_valid():
#         provider = form.save(commit=False)
#         provider.worker = user
#         provider.save()
#         return redirect('shop:list_products')
#     return redirect('shop:home')
