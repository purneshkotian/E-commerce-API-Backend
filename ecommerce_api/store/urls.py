# store/urls.py

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),  # User registration
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),  # List and create products
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),  # Retrieve, update, delete product
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),  # List and create orders
    path('cart/', views.CartRetrieveView.as_view(), name='cart-retrieve'),  # Retrieve cart
    path('cart/items/', views.CartItemCreateView.as_view(), name='cart-item-create'),  # Create cart item
    path('cart/items/<int:pk>/', views.CartItemDestroyView.as_view(), name='cart-item-destroy'),  # Delete cart item

    #jwt token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

