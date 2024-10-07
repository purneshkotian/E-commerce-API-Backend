# store/views.py

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Product, Order, Cart, CartItem
from .serializers import (
    UserRegistrationSerializer,
    ProductSerializer,
    OrderSerializer,
    CartSerializer,
    CartItemSerializer
)


# User Registration View
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to register

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Product List and Create View
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access


# Product Detail, Update, and Delete View
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


# Order List and Create View
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Cart Retrieve View
class CartRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


# Cart Item Create View
class CartItemCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart=cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Cart Item Destroy View
class CartItemDestroyView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk, cart__user=request.user)
            cart_item.delete()
            return Response({"message": "Item removed from cart."}, status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)
