from django.core.validators import MaxValueValidator
from django.db import models

from clientType.models import ClientType
from country.models import Country


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(blank=False, unique=True, validators=[MaxValueValidator(999)])
    name = models.CharField(max_length=70, blank=False)
    fiscal_number = models.CharField(max_length=100, blank=True, default='')
    vat_number = models.CharField(max_length=100, blank=True, default='')
    clientType = models.ForeignKey(ClientType, on_delete=models.CASCADE, related_name='client_clientType')
    tel_number = models.IntegerField(blank=True, default=0)
    email = models.EmailField(default='')
    address1 = models.CharField(max_length=100, blank=True, default='')
    address2 = models.CharField(max_length=100, blank=True, default='')
    zip_code = models.CharField(max_length=10, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='client_country')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
