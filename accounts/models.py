from django.contrib.auth.models import User
from django.db import models

# # Define the names of the groups
# GROUP_ADMIN = 'Admins Group'
# GROUP_USERS = 'Users Group'

# # Define the permissions you want to grant for each group
# PERMISSION_ADD_PRODUCT = 'add_product'
# PERMISSION_CHANGE_PRODUCT = 'change_product'
# PERMISSION_DELETE_PRODUCT = 'delete_product'


class CustomUser(User):

    # email2 = models.EmailField()

    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return f"{self.username}"


# class Customer(User):

#     # customer_id = models.AutoField(primary_key=True, default=True)
#     phone = models.IntegerField()
#     def __str__(self):
#         return f"{self.username}"