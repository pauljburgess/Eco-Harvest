from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Order, Product, User, OrderLine, Pickup

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['pickup_person', 'pickup']

class OrderLineForm(ModelForm):
    class Meta:
        model = OrderLine
        fields = ['product', 'quantity']
