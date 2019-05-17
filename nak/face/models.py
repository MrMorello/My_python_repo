from django.db import models


# Create your models here.
class Order(models.Model):
    subdivision = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    to_whom = models.CharField(max_length=50)

    name = models.CharField(max_length=100)
    quantity = models.FloatField(verbose_name=None)

    PIECES = 'шт'
    KILOGRAMMS = 'кг'
    METERS = 'м'
    KOMPLEKT = 'кт'
    MEASUREMENTS = (
        (PIECES, 'шт'),
        (KILOGRAMMS, 'кг'),
        (METERS, 'м'),
        (KOMPLEKT, 'кт'),
    )
    measurement = models.CharField(
        max_length=2,
        choices=MEASUREMENTS,
        default=PIECES,
    )

    def is_upperclass(self):
        return self.measurement in (self.PIECES, self.KOMPLEKT)

    def __str__(self):
        return self.name
