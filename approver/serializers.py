from rest_framework import serializers
from approver.models import Approver
from employee.models import Employee
from employee.serializers import EmployeeSerializer


class ApproverSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Approver._meta.get_field('id'), required=False)
    employee = EmployeeSerializer(many=False)

    class Meta:
        model = Approver
        extra_kwargs = {
            'id': {'validators': []},
            'employee': {'validators': []},
        }
        fields = ('id',
                  'employee',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        if employee_data:
            employee = Employee.objects.get_or_create(id=employee_data['id'])[0]
            validated_data['employee'] = employee
        return Approver.objects.create(**validated_data)

    def update(self, instance, validated_data):
        employee_data = validated_data.pop('employee')
        if employee_data:
            employee = Employee.objects.get_or_create(id=employee_data['id'])[0]
            validated_data['employee'] = employee
        instance.employee = validated_data.get('employee', instance.employee)
        instance.save()
        return instance
