from django.contrib import admin
from apps.cart_shopping.cart_shopping import CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product','quantity', 'added_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('added_at',)
    