from rest_framework import serializers
from .models import Shopping_Cart



class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping_Cart
        fields = ('id','user','products','total_price', 'status')
