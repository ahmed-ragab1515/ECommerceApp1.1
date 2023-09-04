from django.contrib import admin
from .models import CustomUser #Customer

admin.site.register(CustomUser)

# admin.site.register(Customer)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser, Customer

# class CustomUserAdmin(UserAdmin):
#     list_display = ('username',)  # Display only 'username' in the admin panel
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#     )

# admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.register(Customer)