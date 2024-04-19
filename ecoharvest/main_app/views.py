from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'home.html')

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {
        'products': products
    })
def products_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'products/detail.html', { 'product': product })