from django.db import models

from department.models import Department
from country.models import Country
from myproject import settings


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, on_delete=models.CASCADE, related_name='employee_user')
    personal_number = models.CharField(max_length=8, unique=True, blank=False, default='')
    first_name = models.CharField(max_length=70, blank=False, default='')
    last_name = models.CharField(max_length=70, blank=False, default='')
    birthday = models.DateField(blank=True, default='')
    gender = models.BooleanField(blank=True, default=0)
    tel_number = models.BigIntegerField(blank=True, default=0)
    internal_number = models.IntegerField(blank=True, default=0)
    email = models.EmailField(blank=True, default='')
    driver_license = models.BooleanField(blank=True, default='')
    position = models.CharField(max_length=70, blank=True, default='')
    title = models.CharField(max_length=70, blank=True, default='')
    authorized_approver = models.BooleanField(blank=True, default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employee_department')
    responsible = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='employee_responsible')
    address1 = models.CharField(max_length=100, blank=True, default='')
    address2 = models.CharField(max_length=100, blank=True, default='')
    zip_code = models.CharField(max_length=10, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='employee_country')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
