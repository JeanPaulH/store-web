from django.contrib import admin
from apps.products.products import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','stock','created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)