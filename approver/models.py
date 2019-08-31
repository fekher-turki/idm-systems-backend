from django.db import models

from employee.models import Employee


class Approver(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.OneToOneField(Employee, blank=False, unique=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
