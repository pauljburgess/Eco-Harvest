from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Order, Product, QUANTITIES, User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer','date', 'products', 'quantity']

