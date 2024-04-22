from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Order, Product, User

class OrderForm(ModelForm):
    # products = forms.ModelMultipleChoiceField(
    #     queryset=Product.objects.all()
    # )

    class Meta:
        model = Order
        fields = ['products']

