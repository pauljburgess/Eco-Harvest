from django import forms
from django.forms import ModelForm
from .models import Order, Product

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['date' , 'quantity']
        products = forms.ModelMultipleChoiceField(
            queryset= Product.objects.all()
        )


