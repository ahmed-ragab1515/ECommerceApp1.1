from .models import Order
from .serializers import OrderSerializer
from Shopping_Cart.serializers import ShoppingCartSerializer
from rest_framework import status
# from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from Products.models import Product
from django.core.paginator import Paginator


class OrderAPIView(APIView):

    # def get(self, request):
    #     queryset = Order.objects.all()
    #     serializer = OrderSerializer(queryset, many = True)
    #     if serializer.data:
    #         return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
    #     return JsonResponse({'error': 'No Orders found', 'code':204}, status=status.HTTP_204_NO_CONTENT)
    
    # def get(self, request):
    #     queryset = Order.objects.all()
    #     serializer = OrderSerializer(queryset, many=True)

    #     if not serializer.data:
    #         return JsonResponse({'error': 'No Orders found', 'code': 404}, status=status.HTTP_404_NOT_FOUND)

    #     return JsonResponse({'data': serializer.data, 'code': 200}, status=status.HTTP_200_OK)
    
    # def get(self, request):
    #     queryset = Order.objects.all()
    #     serializer = OrderSerializer(queryset, many=True)
        
    #     if not serializer.data:
    #         return JsonResponse({'error': 'No Orders found', 'code': 404}, status=status.HTTP_404_NOT_FOUND)

    #     return JsonResponse({'data': serializer.data, 'code': 200}, status=status.HTTP_200_OK)
        
    def get(self, request):
        page_number = request.GET.get('page')
        orders = Order.objects.all()
        if orders:
            paginator = Paginator(orders, 2)
            try:
                current_page = paginator.page(page_number)
            except Exception:
                return JsonResponse({'error': 'Page not found', 'code': 404}, status=status.HTTP_404_NOT_FOUND)

            serializer = OrderSerializer(current_page, many = True)
            data = {
                'data': serializer.data,
                'page_number': current_page.number,
                'total_pages': paginator.num_pages,
                'code': 200
            }
            return JsonResponse(data, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'No Orders found', 'code':204}, status=status.HTTP_204_NO_CONTENT)
    



    # def post(self, request):
    #     serializer = OrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
    #     return JsonResponse({'error': serializer.errors, 'code':400}, status=status.HTTP_400_BAD_REQUEST)
    

    # def post(self, request):
    #     data = request.data
    #     if data.get('status') == 'pending':
    #         serializer = ShoppingCartSerializer(data=request.data)
    #     elif data.get('status') == 'shipped' or 'delivered':
    #         serializer = OrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
    #     return JsonResponse({'error': serializer.errors, 'code':400}, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        product_id = request.data.get('products')
        out_of_stock_products = []
        for id in product_id:
            product = Product.objects.get(id=int(id))
            if product.quantity <= 0:

                out_of_stock_products.append(product.name)

        if out_of_stock_products:
            return JsonResponse({'error': f'Products {", ".join(out_of_stock_products)} are not available', 'code': 404}, status=status.HTTP_404_NOT_FOUND)
        
        for id in product_id:
            product = Product.objects.get(id=int(id))
            if product.quantity >= 1:
                product.quantity -= 1
                product.save()
                
        data = request.data
        if data.get('status') == 'pending':
            serializer = ShoppingCartSerializer(data=request.data)
        elif data.get('status') == 'shipped' or 'delivered':
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
        if order:
            serializer = OrderSerializer(order)
            return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Order not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        order = self.get_object(pk)
        if order:
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
            return JsonResponse({'error': serializer.errors, 'code': 400 }, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'error': 'Order not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request,pk):
        order = self.get_object(pk)
        if order:
            order.delete()
            return JsonResponse({'message': 'Order deleted', 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Order not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)




    # def post(self, request):
    #     # Assuming you have some logic to create the order, retrieve the product, and validate the order

    #     product_id = request.data.get('products')  # Assuming you have a 'product_id' field in your data
    #     print(product_id)
    #     for id in product_id:

    #         product_id_int = int(id)
            
    #     product = Product.objects.get(id=product_id_int)
        
    #     # try:
    #     #     product = Product.objects.get(id=product_id)
    #     # except Product.DoesNotExist:
    #     #     return JsonResponse({'error': 'Product not found','code':404}, status=status.HTTP_404_NOT_FOUND)

    #     # Check if the product is available
    #     if product.quantity >= 1:
    #         # Reduce the product quantity by 1
    #         product.quantity -= 1
    #         product.save()
    #         data = request.data
    #         if data.get('status') == 'pending':
    #             serializer = ShoppingCartSerializer(data=request.data)
    #         elif data.get('status') == 'shipped' or 'delivered':
    #             serializer = OrderSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
    #         return JsonResponse({'error': serializer.errors, 'code':400}, status=status.HTTP_400_BAD_REQUEST)

    #     else:
    #         # Return an error JSON response if the product is out of stock
    #         return JsonResponse({'error': 'Product out of stock','code':404}, status=status.HTTP_404_NOT_FOUND)