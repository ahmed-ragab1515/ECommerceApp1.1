from django.contrib import admin
from .models import Order, Order_Status_History #Shopping_Cart

admin.site.register(Order)
admin.site.register(Order_Status_History)
# admin.site.register(Shopping_Cart)
