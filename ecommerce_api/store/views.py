from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import CartItemSerializer, CartSerializer, OrderSerializer, ProductSerializer
from .models import Order, Cart, CartItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
# List all products or create a new product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Retrieve, update, or delete a product by ID
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# List all orders for the logged-in user
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Only return orders belonging to the logged-in user
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the new order
        serializer.save(user=self.request.user)


# Get the cart of the logged-in user
class CartRetrieveView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Get or create a cart for the logged-in user
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart

# Add an item to the cart
class CartItemCreateView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Get the cart for the logged-in user
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

# Remove an item from the cart
class CartItemDestroyView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]