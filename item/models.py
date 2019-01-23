from django.db import models
from django.utils import timezone
from unit.models import Unit


class Item(models.Model):
    iname = models.CharField(max_length=20)
    unit = models.ForeignKey(Unit, related_name="items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.iname



