from django.db import models

from company.models import Company


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=8, unique=True, blank=False, default='')
    name = models.CharField(max_length=70, blank=True, default='')
    company = models.ForeignKey(Company, blank=False, on_delete=models.CASCADE, related_name='department_company')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
