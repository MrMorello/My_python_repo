from django.db import models


# Create your models here.
class Orders(models.Model):
    date_time = models.DateTimeField
    subdivision = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    to_whom = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.subdivision, self.to_whom)


class Names(models.Model):
    name = models.CharField(max_length=100)
    quality = models.FloatField

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

    Orders = models.ForeignKey(Orders, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
