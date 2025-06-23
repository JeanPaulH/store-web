from django.db import models
from apps.orders.orders import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=50)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')  