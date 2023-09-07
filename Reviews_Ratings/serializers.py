from rest_framework import serializers
from .models import Review_Product


class ReviewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review_Product
        fields = ('__all__')
