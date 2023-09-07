from .models import Product
from .serializers import ProductDetailsSerializer, AllProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from django.core.paginator import Paginator
# from .models import Review_Product
# from .serializers import ReviewProductSerializer


class ProductAPIView(APIView):


    # def get(self, request):
    #     products = Product.objects.all()
    #     if products is not None:
    #         serializer = AllProductSerializer(products, many=True)
    #         return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
    #     return JsonResponse({'error': 'No Products found', 'code':204}, status=status.HTTP_204_NO_CONTENT)


    # def get(self, request):
    #     page_number = request.GET.get('page')
    #     products = Product.objects.all()
    #     paginator = Paginator(products, 10)
    #     try:
    #         current_page = paginator.page(page_number)
    #     except Exception:
    #         return JsonResponse({'error': 'Page not found', 'code': 404}, status=status.HTTP_404_NOT_FOUND)
    #     if products is not None:
    #         serializer = AllProductSerializer(products, many=True)
    #         return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
    #     return JsonResponse({'error': 'No Products found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request):
        page_number = request.GET.get('page')
        products = Product.objects.all()
        if products:
            paginator = Paginator(products, 2) 
            try:
                current_page = paginator.page(page_number)
            except Exception:
                return JsonResponse({'error': 'Page not found', 'code': 404}, status=status.HTTP_404_NOT_FOUND)

            serializer = AllProductSerializer(current_page, many=True)
            data = {
                'data': serializer.data,
                'page_number': current_page.number,
                'total_pages': paginator.num_pages,
                'code': 200
            }
            return JsonResponse(data, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'No Products found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = ProductDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
        return JsonResponse({'error': serializer.errors, 'code':400}, status=status.HTTP_400_BAD_REQUEST)
        


class ProductAPIView_pk(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if product:
            serializer = ProductDetailsSerializer(product)
            return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Product not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        product = self.get_object(pk)
        if product:
            serializer = ProductDetailsSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
            return JsonResponse({'error': serializer.errors, 'code': 400 }, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'error': 'Product not found', 'code':204 }, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if product:
            product.delete()
            return JsonResponse({'message': 'Product deleted', 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Product not found', 'code':204 }, status=status.HTTP_204_NO_CONTENT)




#-------------------------------------------------------------------------------



class ProductSearchAPIView(APIView):
    def get(self, request):
        query = request.GET.get('search')
        products = ''
        if query:
            products = Product.objects.filter(name__icontains=query)
            serializer = ProductDetailsSerializer(products, many=True)
            return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
        return JsonResponse({'message': 'Not Found', 'code':204}, status=status.HTTP_204_NO_CONTENT)



#-------------------------------------------------------------------------------



# class ProductReviewListView(APIView):

#     def initial(self, request, *args, **kwargs):
#         super().initial(request, *args, **kwargs)
#         self.csrf_exempt = True  # Bypass CSRF protection

#     def get(self, request):
#         reviews = Review_Product.objects.all()
#         if reviews:
#             serializer = ReviewProductSerializer(reviews, many=True)
#             return JsonResponse({'data': serializer.data, 'code': 200}, status=status.HTTP_200_OK)
#         return JsonResponse({'error': 'No Products found', 'code': 204}, status=status.HTTP_204_NO_CONTENT)

#     def post(self, request):
#         serializer = ReviewProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'data': serializer.data, 'code': 200}, status=status.HTTP_200_OK)
#         return JsonResponse({'error': serializer.errors, 'code': 400}, status=status.HTTP_400_BAD_REQUEST)


# class ProductReview_pk(APIView):

#     def get_object(self, pk):
#         try:
#             return Review_Product.objects.get(pk=pk)
#         except Review_Product.DoesNotExist:
#             return None
        

#     def get(self, request, pk):
    
#         review = self.get_object(pk)
#         if review is not None:
#             serializer = ReviewProductSerializer(review)
#             return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
#         return JsonResponse({'error': 'Product not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)


#     def put(self, request, pk):
#         review = self.get_object(pk)
#         serializer = ReviewProductSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
#         return JsonResponse({'error': serializer.errors, 'code':400}, status=status.HTTP_400_BAD_REQUEST)

    
#     # def delete(self, request, pk):
#     #     review = self.get_object(pk)
#     #     if review is not None:
#     #         review.delete()
#     #         return JsonResponse({'message': 'Product deleted', 'code':200 }, status=status.HTTP_200_OK)
#     #     return JsonResponse({'error': 'Product not found', 'code':204 }, status=status.HTTP_204_NO_CONTENT)
