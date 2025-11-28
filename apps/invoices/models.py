from django.db import models
from django.utils import timezone
from apps.products.models import Product


class Invoice(models.Model):
    number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.number

    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        related_name="items",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
    def price(self):
        return self.product.price

    def total(self):
        return self.quantity * self.product.price
