from django.urls import path
from .views import *


urlpatterns = [
    path('add_order/', OrderAPIView.as_view(), name= 'add_order'),
    path('get_orders/', OrderAPIView.as_view(), name= 'get_orders'),
    path('update_order/<int:pk>/', OrderAPIView_pk.as_view(), name= 'update_order'),
    path('delete_order/<int:pk>/', OrderAPIView_pk.as_view(), name= 'delete_order'),

    path('get_orders/<int:pk>/', OrderAPIView_pk.as_view()),
    


]