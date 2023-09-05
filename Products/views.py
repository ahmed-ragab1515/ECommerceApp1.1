from .models import Product
from .serializers import ProductDetailsSerializer, AllProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Review_Product
from .serializers import ReviewProductSerializer


class ProductAPIView(APIView):


    def get(self, request):
        products = Product.objects.all()
        if products is not None:
            serializer = AllProductSerializer(products, many=True)
            return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
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
        if product is not None:
            serializer = ProductDetailsSerializer(product)
            return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Product not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        product = self.get_object(pk)
        if product is not None:
            serializer = ProductDetailsSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
            return JsonResponse({'error': serializer.errors, 'code': 400 }, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'error': 'Product not found', 'code':204 }, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if product is not None:
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



class ProductReviewListView(APIView):

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.csrf_exempt = True  # Bypass CSRF protection

    def get(self, request):
        reviews = Review_Product.objects.all()
        if reviews:
            serializer = ReviewProductSerializer(reviews, many=True)
            return JsonResponse({'data': serializer.data, 'code': 200}, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'No Products found', 'code': 204}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = ReviewProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data, 'code': 200}, status=status.HTTP_200_OK)
        return JsonResponse({'error': serializer.errors, 'code': 400}, status=status.HTTP_400_BAD_REQUEST)


class ProductReview_pk(APIView):

    def get_object(self, pk):
        try:
            return Review_Product.objects.get(pk=pk)
        except Review_Product.DoesNotExist:
            return None
        

    def get(self, request, pk):
    
        review = self.get_object(pk)
        if review is not None:
            serializer = ReviewProductSerializer(review)
            return JsonResponse({'data': serializer.data, 'code':200 }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Product not found', 'code':204}, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewProductSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data, 'code':200}, status=status.HTTP_200_OK)
        return JsonResponse({'error': serializer.errors, 'code':400}, status=status.HTTP_400_BAD_REQUEST)

    
    # def delete(self, request, pk):
    #     review = self.get_object(pk)
    #     if review is not None:
    #         review.delete()
    #         return JsonResponse({'message': 'Product deleted', 'code':200 }, status=status.HTTP_200_OK)
    #     return JsonResponse({'error': 'Product not found', 'code':204 }, status=status.HTTP_204_NO_CONTENT)
