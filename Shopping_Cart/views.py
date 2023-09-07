from .models import Shopping_Cart
from .serializers import ShoppingCartSerializer
from rest_framework import status
# from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from Products.models import Product
from django.core.paginator import Paginator


class ShoppingCartAPIView(APIView):

    def get(self, request):
        page_number = request.GET.get('page')
        shopping_orders = Shopping_Cart.objects.all()
        if shopping_orders:
            paginator = Paginator(shopping_orders, 2)
            try:
                current_page = paginator.page(page_number)
            except Exception:
                return JsonResponse({'error': 'Page not found', 'code': 404}, status=status.HTTP_404_NOT_FOUND)

            serializer = ShoppingCartSerializer(current_page, many = True)
            data = {
                'data': serializer.data,
                'page_number': current_page.number,
                'total_pages': paginator.num_pages,
                'code': 200
            }

            return JsonResponse(data, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'No Orders found', 'code':204}, status=status.HTTP_204_NO_CONTENT)
    

class ShoppingCartAPIView_pk(APIView):
    def get_object(self, pk):
        try:
            return Shopping_Cart.objects.get(pk=pk)
        except Shopping_Cart.DoesNotExist:
            return None
    
    def get(self, request, pk):
        shopping_order = self.get_object(pk)
        if shopping_order:
            serializer = ShoppingCartSerializer(shopping_order)
            return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Order not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        shopping_order = self.get_object(pk)
        if shopping_order :
            serializer = ShoppingCartSerializer(shopping_order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
            return JsonResponse({'error': serializer.errors, 'code': 400 }, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'error': 'Order not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        shopping_order = self.get_object(pk)
        if shopping_order :
            shopping_order.delete()
            return JsonResponse({'message': 'Order deleted', 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Order not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

