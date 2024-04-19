from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def products_index(request):
    return render(request, 'products/index.html', {
        'products': products
    })