# store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Product endpoints
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    # Order endpoints
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),

    # Cart endpoints
    path('cart/', views.CartRetrieveView.as_view(), name='cart-retrieve'),
    path('cart/items/', views.CartItemCreateView.as_view(), name='cart-item-create'),
    path('cart/items/<int:pk>/', views.CartItemDestroyView.as_view(), name='cart-item-destroy'),
]
