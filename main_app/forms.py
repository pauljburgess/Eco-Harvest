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

class PickupForm(ModelForm):
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.none(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Pickup
        fields = ['products']
    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', None)
        super().__init__(*args, **kwargs)
        if queryset is not None:
            self.fields['products'].queryset = queryset
