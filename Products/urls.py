from django.urls import path
from .views import *


urlpatterns = [
    path('add_product/', ProductAPIView.as_view(), name= 'add_product'),
    path('get_products/', ProductAPIView.as_view(), name= 'get_products'),
    path('update_product/<int:pk>/', ProductAPIView_pk.as_view(), name= 'update_product'),
    path('delete_product/<int:pk>/', ProductAPIView_pk.as_view(), name= 'delete_product'),

    path('get_products_details/<int:pk>/', ProductAPIView_pk.as_view()),
    path('search_products/', ProductSearchAPIView.as_view(), name='search_product'),




    path('add_review/', ProductReviewListView.as_view(), name='add_review'),
    path('reviews/', ProductReviewListView.as_view(), name='review_product'),
    path('reviews/<int:pk>/', ProductReview_pk.as_view(), name='review-product-detail'),

]
