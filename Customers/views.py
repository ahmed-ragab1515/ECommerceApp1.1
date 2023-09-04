from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse
from .models import *

from django.contrib.auth import login
from django.contrib.auth.models import Group, Permission
from .forms import CustomerCreationForm
import json
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import AllowAny


# # Retrieve the permission objects
# permission_add_order = Permission.objects.get(codename=PERMISSION_ADD_ORDER)
# permission_change_order = Permission.objects.get(codename=PERMISSION_CHANGE_ORDER)
# permission_delete_order = Permission.objects.get(codename=PERMISSION_DELETE_ORDER)
# permission_view_order = Permission.objects.get(codename=PERMISSION_VIEW_ORDER)

# # Create or get the groups
# group_customers, created = Group.objects.get_or_create(name=GROUP_CUSTOMERS)

# # Assign the permissions to the groups
# group_customers.permissions.add(permission_add_order, permission_change_order, permission_delete_order, permission_view_order)


@csrf_exempt
def customer_login(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            # Create an instance of the AuthenticationForm with the parsed JSON data
            form = AuthenticationForm(request, data=data)
            # Check if the form is valid
            if form.is_valid():
                # Log the user in
                user = form.get_user()
                login(request, user)
                # Generate access token using Simple JWT
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                # Return the access token in the JSON response
                return JsonResponse({'access_token': access_token, 'code':200}, status=status.HTTP_200_OK)
            else:
                # Return a JSON response with the errors for invalid login
                return JsonResponse({'error': form.errors, 'code':400}, status=status.HTTP_400_BAD_REQUEST)

        except json.decoder.JSONDecodeError as e:
            # Return a JSON response for invalid JSON format in the request body
            return JsonResponse({'error': 'Invalid JSON format', 'code':400}, status=status.HTTP_400_BAD_REQUEST)

    else:
        # Return a JSON response for invalid request method (GET, PUT, etc.)
        return JsonResponse({'error': 'Invalid request method', 'code':405}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Django Creation form

@csrf_exempt
@api_view(['POST'])
@authentication_classes([])  # Empty list to remove authentication classes
@permission_classes([AllowAny])
def customer_signup(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)

            # Create an instance of the CustomUserCreationForm with the parsed JSON data
            form = CustomerCreationForm(data=data)

            # Check if the form is valid
            if form.is_valid():
                user = form.save()
                # login(request, user)
                # user.groups.add(group_customers)

                # Return a JSON response for successful signup
                return JsonResponse({'message': 'Signup Success', 'code':200}, status=status.HTTP_200_OK)

            else:
                # Return a JSON response with the errors for invalid signup
                errors_json = form.errors.as_json()
                return JsonResponse({'error': errors_json, 'code':406}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except json.decoder.JSONDecodeError as e:
            # Return a JSON response for invalid JSON format in the request body
            return JsonResponse({'error': 'Invalid JSON format', 'code':400}, status=status.HTTP_400_BAD_REQUEST)

    else:
        # Return a JSON response for invalid request method (GET, PUT, etc.)
        return JsonResponse({'error': 'Invalid request method', 'code':405}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            


