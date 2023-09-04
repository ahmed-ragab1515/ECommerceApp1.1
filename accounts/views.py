from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import CustomUserSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login
import json
from rest_framework.views import APIView
from .models import CustomUser

class UserRegistrationView(APIView):
    @csrf_exempt  
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            ###########
            # user = serializer.save()
            user = CustomUser.objects.create_user(username=username, password=password)
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

#########################( Customers )#############################

