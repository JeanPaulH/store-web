from django.db import models
from apps.products.products import Product

class SEOData(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField(blank=True)
    keywords = models.CharField(max_length=255, blank=True)