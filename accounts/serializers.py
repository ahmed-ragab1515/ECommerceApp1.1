from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = ('id', 'username','password', 'role', 'email2', 'email') 
        fields = ('__all__') 


# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
# from rest_framework import serializers

# class CustomUserSerializer(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('username', 'password1', 'password2', 'email',)  # Add your custom fields here

        

















        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('customer_id', 'phone',) 