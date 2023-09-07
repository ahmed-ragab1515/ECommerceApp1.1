from django.contrib import admin
from .models import Product, Product_Category, Product_Image

admin.site.register(Product)
admin.site.register(Product_Category)
# admin.site.register(Review_Product)
admin.site.register(Product_Image)