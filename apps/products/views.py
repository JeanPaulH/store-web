from django.shortcuts import render
from rest_framework import viewsets
from apps.products.products import Product
from apps.products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer