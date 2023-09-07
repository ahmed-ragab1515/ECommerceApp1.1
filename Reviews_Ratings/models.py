from django.db import models
from Products.models import Product
from accounts.models import CustomUser 


class Review_Product(models.Model):
    review_title = models.CharField(max_length=100, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
    text_review = models.TextField(blank=True)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    review_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review {self.review_title} for product {self.product.name} by {self.user.username}"
    
    class Meta:
        ordering = ['review_date']
