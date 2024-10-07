# store/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Order, Cart, CartItem


# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        # Create a new user with the given data, and hash the password automatically
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'created_at', 'updated_at']


# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'total_price', 'status', 'created_at']


# Cart Item Serializer
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'created_at']


# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at']
