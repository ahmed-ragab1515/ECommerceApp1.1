from rest_framework import serializers
from .models import Product, Review_Product

class ProductDetailsSerializer (serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = ('__all__')

class AllProductSerializer (serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = ('id','name', 'price')

class ReviewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review_Product
        fields = '__all__'
