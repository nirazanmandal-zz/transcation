from django.db import models


# Create your models here.
class Customer(models.Model):
    cname = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "customer"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return str(self.cname)
