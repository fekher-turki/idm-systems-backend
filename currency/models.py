from django.db import models


class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=8, unique=True, blank=False, default='')
    description = models.CharField(max_length=140, blank=True, default='')
    decimal_place = models.IntegerField(blank=False, default=0)
    symbol = models.CharField(max_length=5, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
