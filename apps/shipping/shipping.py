from django.db import models
from apps.orders.orders import Order

class ShippingDetail(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    shipped_at = models.DateTimeField(null=True, blank=True)
    tracking_number = models.CharField(max_length=100, blank=True)