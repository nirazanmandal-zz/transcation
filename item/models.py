from django.db import models

from unit.models import Unit


class Item(models.Model):
    name = models.CharField(max_length=20)
    unit = models.ForeignKey(Unit, related_name="items", on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
        db_table = 'items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
