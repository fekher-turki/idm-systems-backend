from django.db import models

from currency.models import Currency


class ExchangeRate(models.Model):
    id = models.AutoField(primary_key=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='exchangeRate_currency')
    value = models.FloatField(blank=False, default=0)
    date = models.DateField(blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
