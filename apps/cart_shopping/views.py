from django.shortcuts import render
from rest_framework import viewsets
from apps.cart_shopping.cart_shopping import CartItem
from apps.cart_shopping.serializers import CartItemSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer