from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import CustomUserSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login
import json
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

class UserRegistrationView(APIView):
    @csrf_exempt  
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            # password = serializer.validated_data.get('password')
            # serializer.validated_data['password']=make_password(password)
            ###########
            user = serializer.save()
            # user = CustomUser.objects.create_user(username=username, password=password)
            ###########
            # user = serializer.save(commit=False)
            # user.set_password(data.password)
            # user.save()
            response_data = {
                'message': 'User registered successfully',
                'user_id': user.id,
            }
            return JsonResponse({'message': response_data, 'code': 201}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'error': serializer.errors, 'code': 406}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def get(self, request):
        return JsonResponse({'message': 'Invalid request method', 'code': 405}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


class UserLoginView(APIView):
    @csrf_exempt  
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful', 'code': 200}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'Login failed', 'code': 401}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        return JsonResponse({'message': 'Invalid request method', 'code': 405}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ChangePasswordView(APIView):

    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        new_password = data.get('new_password')

        User = get_user_model()

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                user.set_password(new_password)
                user.save()
                return JsonResponse({'message': 'Password changed successfully', 'code': 200}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error': 'Old password is incorrect', 'code': 401}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found', 'code': 401}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        return JsonResponse({'message': 'GET request to change password not supported', 'code': 405}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#########################( Customers )#############################

