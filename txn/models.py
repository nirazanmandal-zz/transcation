from django.db import models
from customer.models import Customer
from item.models import Item


class Transactions(models.Model):
    cname = models.ForeignKey(Customer, related_name="transactions", on_delete=models.DO_NOTHING)
    itemname = models.ForeignKey(Item, related_name='itemname', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=120)
    total = models.CharField(max_length=120)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'transactions'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return self.cname

    def clean(self):
        pass
