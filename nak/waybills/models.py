from django.db import models


class Zayavka(models.Model):
    osnovanie = models.CharField(max_length=128, blank=True, null=True, default=None)
    podrazdeleine = models.CharField(max_length=128, blank=True, null=True, default=None)
    commentary = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.osnovanie

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Tovar(models.Model):
    zayavka = models.ForeignKey(Zayavka, blank=True, null=True, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
