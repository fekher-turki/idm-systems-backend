from datetime import date

from django.db import models

from client.models import Client
from company.models import Company
from sourceType.models import SourceType


class Source(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=8, unique=True, blank=True, default='')
    description = models.CharField(max_length=70, blank=True, default='')
    sourceType = models.ForeignKey(SourceType, on_delete=models.CASCADE, related_name='source_sourceType')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='source_client')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='source_company')
    date_start = models.DateField(blank=True, default=date.today)
    date_end = models.DateField(blank=True, default=date.today)
    status = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
