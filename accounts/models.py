from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model

# # Define the names of the groups
# GROUP_ADMIN = 'Admins Group'
# GROUP_USERS = 'Users Group'

# # Define the permissions you want to grant for each group
# PERMISSION_ADD_PRODUCT = 'add_product'
# PERMISSION_CHANGE_PRODUCT = 'change_product'
# PERMISSION_DELETE_PRODUCT = 'delete_product'


class CustomUser(User):


    # email2 = models.EmailField(blank=False)

    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    def save(self, *args, **kwargs):
        if self.id is None :
            self.password = make_password(self.password)

        super(User, self).save(*args, **kwargs)
    

    def __str__(self):
        return f"{self.username}"
    
    # def change_password(self, username, password, new_password):
    #     User = get_user_model()
    #     try:
    #         user = User.objects.get(username=username)
    #         if check_password(password, user.password):
    #             user.set_password(new_password)
    #             user.save()
    #         else:
    #             raise ValueError("Old password does not match.")
    #     except User.DoesNotExist:
    #         raise ValueError("User not found.")


# class Customer(User):

#     # customer_id = models.AutoField(primary_key=True, default=True)
#     phone = models.IntegerField()
#     def __str__(self):
#         return f"{self.username}"