from django.db import models
from django.contrib.auth.models import User
# Create your models here.

QUANTITIES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    owner = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('The Order Date was:')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(
        max_length=1,
        choices=QUANTITIES,
        default=QUANTITIES[0][0]
    )

    def __str__(self):
        return f"{self.customer} ordered {self.product}"
    
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)   

    def __str__(self):
        return f"Photo for product_id: {self.product_id} @{self.url}"