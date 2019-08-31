from django.db import models


class Rule(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(blank=False, default='')
    value = models.IntegerField(blank=False, default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
