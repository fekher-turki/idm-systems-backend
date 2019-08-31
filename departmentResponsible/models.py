from django.db import models

from department.models import Department
from employee.models import Employee


class DepartmentResponsible(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.OneToOneField(Department, on_delete=models.CASCADE, unique=True, related_name='departmentResponsible_department')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='departmentResponsible_employee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('department', 'employee',)

    def __int__(self):
        return self.id
