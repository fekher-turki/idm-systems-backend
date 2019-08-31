from rest_framework import serializers

from client.models import Client
from clientType.models import ClientType
from clientType.serializers import ClientTypeSerializer
from country.models import Country
from country.serializers import CountrySerializer


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Client._meta.get_field('id'), required=False)
    country = CountrySerializer(many=False)
    clientType = ClientTypeSerializer(many=False)

    class Meta:
        model = Client
        extra_kwargs = {
            'code': {'validators': []},
        }
        fields = ('id',
                  'code',
                  'name',
                  'fiscal_number',
                  'vat_number',
                  'clientType',
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
        clientType_data = validated_data.pop('clientType')
        if clientType_data:
            clientType = ClientType.objects.get_or_create(id=clientType_data['id'])[0]
            validated_data['clientType'] = clientType
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        country_data = validated_data.pop('country')
        if country_data:
            country = Country.objects.get_or_create(id=country_data['id'])[0]
            validated_data['country'] = country
        clientType_data = validated_data.pop('clientType')
        if clientType_data:
            clientType = ClientType.objects.get_or_create(id=clientType_data['id'])[0]
            validated_data['clientType'] = clientType
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.fiscal_number = validated_data.get('fiscal_number', instance.fiscal_number)
        instance.vat_number = validated_data.get('vat_number', instance.vat_number)
        instance.clientType = validated_data.get('clientType', instance.clientType)
        instance.tel_number = validated_data.get('tel_number', instance.tel_number)
        instance.email = validated_data.get('email', instance.email)
        instance.address1 = validated_data.get('address1', instance.address1)
        instance.address2 = validated_data.get('address2', instance.address2)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance
