from django.db import models
from accounts.models import CustomUser 


class Product_category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return f"{self.category_name}"


class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, unique=True )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    category_of_product = models.ForeignKey(Product_category, on_delete=models.CASCADE, blank=True, default=True)

    def __str__(self):
        return f"{self.name}"
    

class Review_Product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, default=True)
    text_review = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"