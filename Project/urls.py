from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    # path('',include('Customers.urls')),
    path('',include('Orders.urls')),
    path('',include('Products.urls')),
    # path('',include('Review_Product.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
