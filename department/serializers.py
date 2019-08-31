from rest_framework import serializers

from company.models import Company
from company.serializers import CompanySerializer
from department.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Department._meta.get_field('id'), required=False)
    company = CompanySerializer(many=False)

    class Meta:
        model = Department
        extra_kwargs = {
            'code': {'validators': []},
        }
        fields = ('id',
                  'code',
                  'name',
                  'company',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        company_data = validated_data.pop('company')
        if company_data:
            company = Company.objects.get_or_create(id=company_data['id'])[0]
            validated_data['company'] = company
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        company_data = validated_data.pop('company')
        if company_data:
            company = Company.objects.get_or_create(id=company_data['id'])[0]
            validated_data['company'] = company
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance
