from django.contrib import admin
from .models import Product, Order, Photo, Pickup
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Photo)
admin.ste.register(Pickup)