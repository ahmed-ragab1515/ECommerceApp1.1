from django.db import models
from accounts.models import CustomUser
from Products.models import Product



class Shopping_Cart(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
    products = models.ManyToManyField(Product, blank=False)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    )
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='pending')
    order_date = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"Order #{self.pk} By User {self.user} pending in the Shopping Cart"
    
    def calculate_total_price(self):
        total_price = 0 
        for product in self.products.all():
            total_price += product.price
        return total_price

    @property
    def total_price(self):
        return self.calculate_total_price


    class Meta:
        ordering = ['order_date']
