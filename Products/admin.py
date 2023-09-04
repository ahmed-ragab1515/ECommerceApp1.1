from django.contrib import admin
from .models import Product, Product_category, Review_Product

admin.site.register(Product)
admin.site.register(Product_category)
admin.site.register(Review_Product)