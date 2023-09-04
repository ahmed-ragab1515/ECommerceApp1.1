from .models import Order
from .serializers import OrderSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse


class OrderAPIView(APIView):

    def get(self, request):
        queryset = Order.objects.all()
        if queryset is not None:
            serializer = OrderSerializer(queryset, many = True)
            # return Response(serializer.data)
            return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'No Orders found', 'code':204}, status=status.HTTP_204_NO_CONTENT)
        


    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
        return JsonResponse({'error': serializer.errors, 'code':400}, status=status.HTTP_400_BAD_REQUEST)

class OrderAPIView_pk(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return None

    def get(self, request, pk):
        order = self.get_object(pk)
        if order is not None:
            serializer = OrderSerializer(order)
            return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Order not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        order = self.get_object(pk)
        if order is not None:
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
            return JsonResponse({'error': serializer.errors, 'code': 400 }, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'error': 'Order not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        order = self.get_object(pk)
        if order is not None:
            order.delete()
            return JsonResponse({'message': 'Order deleted', 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Order not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)


