from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    # path('',include('Customers.urls')),
    path('',include('Orders.urls')),
    path('',include('Products.urls')),
    # path('',include('Review_Product.urls')),
]
