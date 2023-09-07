from django.urls import path
from .views import *


urlpatterns = [
    path('get_shopping_orders/', ShoppingCartAPIView.as_view(), name= 'get_shopping_orders'),
    path('update_shopping_order/<int:pk>/', ShoppingCartAPIView_pk.as_view(), name= 'update_shopping_order'),
    path('delete_shopping_order/<int:pk>/', ShoppingCartAPIView_pk.as_view(), name= 'delete_shopping_order'),

    path('get_shopping_orders/<int:pk>/', ShoppingCartAPIView_pk.as_view(), name= 'specific_shopping_orders'),


]