from django.urls import path
from .views import *


urlpatterns = [

    path('add_review/', ProductReviewListView.as_view(), name='add_review'),
    path('reviews/', ProductReviewListView.as_view(), name='review_product'),
    path('reviews/<int:pk>/', ProductReview_pk.as_view(), name='review-product-detail'),

]
