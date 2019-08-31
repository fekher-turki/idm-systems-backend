from rest_framework import serializers

from employee.models import Employee
from employee.serializers import EmployeeSerializer
from requester.models import Requester


class RequesterSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Requester._meta.get_field('id'), required=False)
    employee = EmployeeSerializer(many=False)

    class Meta:
        model = Requester
        fields = ('id',
                  'employee',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        if employee_data:
            employee = Employee.objects.get_or_create(id=employee_data['id'])[0]
            validated_data['employee'] = employee
        return Requester.objects.create(**validated_data)

    def update(self, instance, validated_data):
        employee_data = validated_data.pop('employee')
        if employee_data:
            employee = Employee.objects.get_or_create(id=employee_data['id'])[0]
            validated_data['employee'] = employee
        instance.employee = validated_data.get('employee', instance.employee)
        instance.save()
        return instance

