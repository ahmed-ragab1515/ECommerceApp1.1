from django.db import models
from accounts.models import CustomUser 



class Product_Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.category_name}"



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, unique=True )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    category_of_product = models.ForeignKey(Product_Category, on_delete=models.CASCADE, default=1)
    # images = models.ImageField(upload_to='photos/%y/%m/%d')
    images = models.ManyToManyField('Product_Image', blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['id']
    


# class Review_Product(models.Model):
#     review_title = models.CharField(max_length=100, blank=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
#     text_review = models.TextField(blank=True)
#     rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
#     review_date = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Review {self.review_title} for product {self.product.name} by {self.user.username}"
    
#     class Meta:
#         ordering = ['review_date']
    


class Product_Image(models.Model):
    id = models.IntegerField(primary_key=True)
    product2 = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/%y/%m/%d')

    def __str__(self):
        return f"Image for product {self.product2.name}"