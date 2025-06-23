from rest_framework import serializers
from apps.cart_shopping.cart_shopping import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'