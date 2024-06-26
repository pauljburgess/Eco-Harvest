from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

QUANTITIES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)

class Pickup(models.Model):
    date = models.DateField('Pickup Date')
    location = models.CharField('Pickup Location', max_length=250)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return f"{self.location} on {self.date}"
    
    def get_absolute_url(self):
        return reverse('pickup_detail', kwargs={'pickup_id': self.id})

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    owner = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickups = models.ManyToManyField('Pickup')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f"{self.name}" 
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'order_id': self.id})


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_person = models.CharField(max_length=50, default='None')
    date = models.DateField('Order Date', default=str(date.today()))
    pickup = models.ForeignKey(Pickup, on_delete=models.CASCADE, default=1)
   
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

    def line_cost(self):
        return int(self.quantity) * self.product.price
      
    def __str__(self):
        return f"{self.get_quantity_display()} {self.product}"
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)   

    def __str__(self):
        return f"Photo for product_id: {self.product_id} @{self.url}"
    

    def __str__(self):
        return f"{self.location} on {self.date}"