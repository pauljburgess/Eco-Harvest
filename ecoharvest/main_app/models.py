from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

QUANTITIES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    owner = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pickup_person = models.CharField(max_length=50, default='None')
    date = models.DateField('Order Date', default=str(date.today()))
   
    def __str__(self):
        return f"{self.customer} placed an order: Order #{self.id}"
    
    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'order_id': self.id})
    
class OrderLine(models.Model):
    customer = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(
        max_length=1,
        choices=QUANTITIES,
        default=QUANTITIES[0][0]
    )

    def __str__(self):
        return f"{self.get_quantities_display} {self.product}"
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)   

    def __str__(self):
        return f"Photo for product_id: {self.product_id} @{self.url}"
    
class Pickup(models.Model):
    date = models.DateField('Pickup Date')
    location = models.CharField('Pickup Location', max_length=250)