from django.urls import path
from Customers.views import *
from django.contrib.auth.views import *

urlpatterns = [
    path('customer_login/', customer_login, name='login'),
    # path('login/', LoginView.as_view(),{'template_name':'login.html'}, name='login'),
    path('customer_logout/', LogoutView.as_view(), name='logout'),
    # path('logout_success/', logout_success, name='logout_success'),
    path('customer_signup/', customer_signup, name='signup'),
    # path('welcome/', welcome_page, name='welcome'),

]