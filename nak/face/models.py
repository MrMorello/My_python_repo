from django.db import models


# Create your models here.
class Order(models.Model):
    date_time = models.DateTimeField
    subdivision = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    to_whom = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.subdivision, self.to_whom)


class Name(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(verbose_name=None)

    PIECES = 'P'
    KILOGRAMMS = 'KG'
    METERS = 'M'
    KOMPLEKT = 'KT'
    MEASUREMENTS = (
        (PIECES, 'P'),
        (KILOGRAMMS, 'KG'),
        (METERS, 'M'),
        (KOMPLEKT, 'KT'),
    )
    measurement = models.CharField(
        max_length=2,
        choices=MEASUREMENTS,
        default=PIECES,
    )

    def is_upperclass(self):
        return self.measurement in (self.PIECES, self.KOMPLEKT)

    Order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
