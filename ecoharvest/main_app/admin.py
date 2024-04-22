from django.contrib import admin
from .models import Product, Order, Photo
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Photo)