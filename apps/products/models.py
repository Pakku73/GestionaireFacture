from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name
