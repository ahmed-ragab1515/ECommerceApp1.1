from rest_framework import serializers
from .models import Order, Shopping_Cart

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','user','products','total_price', 'status')

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping_Cart
        fields = ('id','user','products','total_price', 'status')
