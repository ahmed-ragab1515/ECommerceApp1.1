from django.urls import path
from .views import UserRegistrationView, UserLoginView, ChangePasswordView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password')
]
