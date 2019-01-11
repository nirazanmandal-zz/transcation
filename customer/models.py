from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = "customer"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name
