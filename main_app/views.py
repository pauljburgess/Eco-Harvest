import os
import uuid
import boto3
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Product, Photo, Order, OrderLine, Pickup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderForm, OrderLineForm, PickupForm
from datetime import date
from django.utils import timezone
from django.urls import reverse


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
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def order(request):
   order_form = OrderForm()
   return render(request, 'order.html', {'order_form': order_form, })

@login_required
def order_detail(request, order_id):
   order = Order.objects.get(id=order_id)
   available_pickups = Pickup.objects.all()
   order_line_form = OrderLineForm()
   return render(request, 'orders/detail.html', {'order' : order, 'order_line_form' : order_line_form, 'pickup': available_pickups })

@login_required
def pickup_detail(request, pickup_id):
   pickups = Pickup.objects.get(id=pickup_id)
   return render(request, 'pickups/detail.html', {'pickups' : pickups })

@login_required
def add_order_line (request, order_id):
  form = OrderLineForm(request.POST)
  print(order_id)
  if form.is_valid():
    new_line = form.save(commit=False)
    new_line.customer = Order.objects.get(id=order_id)
    new_line.save()
  return redirect('order_detail', order_id=order_id)

@login_required
def order_index(request):
   orders = Order.objects.filter(customer=request.user)
   return render(request, 'orders/index.html', {'orders' : orders})  

def pickup_index(request):
   pickups = Pickup.objects.filter(date__gte=timezone.now().date())
   return render(request, 'pickups/index.html', {'pickups' : pickups}) 

class ProductCreate(LoginRequiredMixin, CreateView):
   model = Product
   fields = ['name', 'description', 'price']

   def form_valid(self, form):
        form.instance.user = self.request.user 
        form.instance.owner = self.request.user.username  
        return super().form_valid(form)

   def get_success_url(self):
        return reverse('product_index')
   
class PickupCreate(LoginRequiredMixin, CreateView):
   model = Pickup
   fields = ['location', 'date']

class OrderCreate(LoginRequiredMixin, CreateView):
   model = Order
   fields = ['pickup_person', 'pickup']

   def form_valid(self, form):
      form.instance.customer = self.request.user
      return super().form_valid(form)

class OrderUpdate(LoginRequiredMixin, UpdateView):
   model = Order
   fields = ['pickup_person', 'pickup']

class OrderDelete(LoginRequiredMixin, DeleteView):
   model = Order
   success_url = '/orders/index'

class ProductList(LoginRequiredMixin, ListView):
   model = Product 

class PickupList(LoginRequiredMixin, ListView):
   model = Pickup

@login_required
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

@login_required
def pickup_update(request, pickup_id):
   pickup = Pickup.objects.get(id=pickup_id)
   products = Product.objects.filter(created_by=request.user)
   if request.method == 'POST':
      form = PickupForm(request.POST, queryset=products)
      if form.is_valid():
         products_selected = form.cleaned_data.get('products', [])
         pickup.products.add(*products_selected)
         pickup.save()
         return redirect('pickup_detail', pickup_id=pickup_id)
   else: 
      form = PickupForm(initial={'products' : pickup.products.all()}, queryset=products)
   return render(request, 'pickup_update.html', {'form': form})