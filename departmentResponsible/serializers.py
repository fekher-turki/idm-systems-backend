from rest_framework import serializers

from department.models import Department
from department.serializers import DepartmentSerializer
from departmentResponsible.models import DepartmentResponsible
from employee.models import Employee
from employee.serializers import EmployeeSerializer


class DepartmentResponsibleSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=DepartmentResponsible._meta.get_field('id'), required=False)
    department = DepartmentSerializer(many=False)
    employee = EmployeeSerializer(many=False)

    class Meta:
        model = DepartmentResponsible
        fields = ('id',
                  'department',
                  'employee',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        department_data = validated_data.pop('department')
        if department_data:
            department = Department.objects.get_or_create(id=department_data['id'])[0]
            validated_data['department'] = department
        employee_data = validated_data.pop('employee')
        if employee_data:
            employee = Employee.objects.get_or_create(id=employee_data['id'])[0]
            validated_data['employee'] = employee
        return DepartmentResponsible.objects.create(**validated_data)

    def update(self, instance, validated_data):
        department_data = validated_data.pop('department')
        if department_data:
            department = Department.objects.get_or_create(id=department_data['id'])[0]
            validated_data['department'] = department
        employee_data = validated_data.pop('employee')
        if employee_data:
            employee = Employee.objects.get_or_create(id=employee_data['id'])[0]
            validated_data['employee'] = employee
        instance.department = validated_data.get('department', instance.department)
        instance.employee = validated_data.get('employee', instance.employee)
        instance.save()
        return instance
