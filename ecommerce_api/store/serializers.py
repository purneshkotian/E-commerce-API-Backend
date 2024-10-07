
from rest_framework import serializers
from .models import Product, Order, Cart, CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'created_at']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Include product details in the cart item

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)  # Include all items in the cart

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']