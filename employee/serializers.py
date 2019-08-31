from rest_framework import serializers

from api.models import User
from api.serializers import UserSerializer
from country.models import Country
from department.models import Department
from department.serializers import DepartmentSerializer
from employee.models import Employee
from country.serializers import CountrySerializer


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Employee._meta.get_field('id'), required=False)
    user = UserSerializer(many=False)
    country = CountrySerializer(many=False)
    department = DepartmentSerializer(many=False)

    class Meta:
        model = Employee
        extra_kwargs = {
            'id': {'validators': []},
            'personal_number': {'validators': []},
            'user': {'validators': []},
        }
        fields = ('id',
                  'user',
                  'personal_number',
                  'first_name',
                  'last_name',
                  'birthday',
                  'gender',
                  'tel_number',
                  'internal_number',
                  'email',
                  'driver_license',
                  'position',
                  'title',
                  'authorized_approver',
                  'department',
                  'responsible',
                  'address1',
                  'address2',
                  'zip_code',
                  'city',
                  'country',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        if user_data:
            user = User.objects.get_or_create(id=user_data['id'])[0]
            validated_data['user'] = user
        country_data = validated_data.pop('country')
        if country_data:
            country = Country.objects.get_or_create(id=country_data['id'])[0]
            validated_data['country'] = country
        department_data = validated_data.pop('department')
        if department_data:
            department = Department.objects.get_or_create(id=department_data['id'])[0]
            validated_data['department'] = department
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        if user_data:
            user = User.objects.get_or_create(id=user_data['id'])[0]
            validated_data['user'] = user
        country_data = validated_data.pop('country')
        if country_data:
            country = Country.objects.get_or_create(id=country_data['id'])[0]
            validated_data['country'] = country
        department_data = validated_data.pop('department')
        if department_data:
            department = Department.objects.get_or_create(id=department_data['id'])[0]
            validated_data['department'] = department
        instance.user = validated_data.get('user', instance.user)
        instance.personal_number = validated_data.get('personal_number', instance.personal_number)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.tel_number = validated_data.get('tel_number', instance.tel_number)
        instance.internal_number = validated_data.get('internal_number', instance.internal_number)
        instance.email = validated_data.get('email', instance.email)
        instance.driver_license = validated_data.get('driver_license', instance.driver_license)
        instance.position = validated_data.get('position', instance.position)
        instance.title = validated_data.get('title', instance.title)
        instance.authorized_approver = validated_data.get('authorized_approver', instance.authorized_approver)
        instance.department = validated_data.get('department', instance.department)
        instance.responsible = validated_data.get('responsible', instance.responsible)
        instance.address1 = validated_data.get('address1', instance.address1)
        instance.address2 = validated_data.get('address2', instance.address2)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance
