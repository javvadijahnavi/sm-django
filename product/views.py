from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Discount, Cart, CheckOut
from .serializer import ProductSerializer, DiscountSerializer, CartSerializer, CheckOutSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DiscountViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


@api_view(['GET', 'POST'])
def carts_list_view(request):
    if request.method == 'GET':
        items = Cart.objects.all()
        serializer = CartSerializer(items, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def carts_detail_view(request, pk):
    try:
        cart_item = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response({'response': '404 NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartSerializer(cart_item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cart_item.delete()
        return Response({"response": '204 NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
