from django.core.validators import MaxValueValidator
from django.db import models


class ClientType(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(blank=False, unique=True, validators=[MaxValueValidator(999)])
    name = models.CharField(max_length=70, blank=False)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
