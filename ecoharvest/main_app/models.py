from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    owner = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('Order Date')
    products = models.ManyToManyField(Product)
   
    def __str__(self):
        return f"{self.customer} placed an order: Order #{self.id} "
    
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)   

    def __str__(self):
        return f"Photo for product_id: {self.product_id} @{self.url}"