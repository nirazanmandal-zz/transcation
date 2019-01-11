from django.db import models

from unit.models import Unit


class Item(models.Model):
    name = models.CharField(max_length=20)
    unit = models.ForeignKey(Unit, related_name="items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name
