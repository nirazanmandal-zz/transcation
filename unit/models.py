from django.db import models


# Create your models here.
class Unit(models.Model):
    display_name = models.CharField(max_length=16)
    actual_name = models.CharField(max_length=32)

    class Meta:
        db_table = "unit"
        verbose_name = "unit"
        verbose_name_plural = "units"

    def __str__(self):
        return self.display_name
