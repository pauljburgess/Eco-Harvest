import os
import uuid
import boto3
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Product, Photo, Order, OrderLine
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderForm, OrderLineForm
from datetime import date


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
   return render(request, 'about.html')

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {
        'products': products
    })

def products_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'products/detail.html', { 'product': product })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def order(request):
   order_form = OrderForm()
   return render(request, 'order.html', {'order_form': order_form, })

def order_detail(request, order_id):
   print(order_id)
   order = Order.objects.get(id=order_id)
   order_line_form = OrderLineForm()
   print(order)
   return render(request, 'orders/detail.html', {'order' : order, 'order_line_form' : order_line_form })

def add_order_line (request, order_id):
  form = OrderLineForm(request.POST)
  if form.is_valid():
    new_line = form.save(commit=False)
    new_line.customer = Order.objects.get(id=order_id)
    new_line.save()
  return redirect('order_detail', order_id=order_id)


class OrderCreate(CreateView):
   model = Order
   fields = ['pickup_person']
  
class ProductList(ListView):
   model = Product 

def add_photo(request, product_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        print(os.environ['S3_BUCKET'])
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, product_id=product_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', product_id=product_id)
