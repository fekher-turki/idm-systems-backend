from rest_framework import serializers

from company.models import Company
from country.models import Country
from country.serializers import CountrySerializer


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Company._meta.get_field('id'), required=False)
    country = CountrySerializer(many=False)

    class Meta:
        model = Company
        extra_kwargs = {
            'code': {'validators': []},
        }
        fields = ('id',
                  'code',
                  'name',
                  'fiscal_number',
                  'vat_number',
                  'tel_number',
                  'email',
                  'address1',
                  'address2',
                  'zip_code',
                  'city',
                  'country',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        country_data = validated_data.pop('country')
        if country_data:
            country = Country.objects.get_or_create(id=country_data['id'])[0]
            validated_data['country'] = country
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        country_data = validated_data.pop('country')
        if country_data:
            country = Country.objects.get_or_create(id=country_data['id'])[0]
            validated_data['country'] = country
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.fiscal_number = validated_data.get('fiscal_number', instance.fiscal_number)
        instance.vat_number = validated_data.get('vat_number', instance.vat_number)
        instance.tel_number = validated_data.get('tel_number', instance.tel_number)
        instance.email = validated_data.get('email', instance.email)
        instance.address1 = validated_data.get('address1', instance.address1)
        instance.address2 = validated_data.get('address2', instance.address2)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance
