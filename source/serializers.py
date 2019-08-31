from rest_framework import serializers

from client.models import Client
from client.serializers import ClientSerializer
from company.models import Company
from company.serializers import CompanySerializer
from source.models import Source
from sourceType.models import SourceType
from sourceType.serializers import SourceTypeSerializer


class SourceSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Source._meta.get_field('id'), required=False)
    sourceType = SourceTypeSerializer(many=False)
    client = ClientSerializer(many=False)
    company = CompanySerializer(many=False)

    class Meta:
        model = Source
        extra_kwargs = {
            'id': {'validators': []},
            'code': {'validators': []},
        }
        fields = ('id',
                  'code',
                  'description',
                  'sourceType',
                  'client',
                  'company',
                  'date_start',
                  'date_end',
                  'status',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        sourceType_data = validated_data.pop('sourceType')
        if sourceType_data:
            sourceType = SourceType.objects.get_or_create(id=sourceType_data['id'])[0]
            validated_data['sourceType'] = sourceType
        client_data = validated_data.pop('client')
        if client_data:
            client = Client.objects.get_or_create(id=client_data['id'])[0]
            validated_data['client'] = client
        company_data = validated_data.pop('company')
        if company_data:
            company = Company.objects.get_or_create(id=company_data['id'])[0]
            validated_data['company'] = company
        return Source.objects.create(**validated_data)

    def update(self, instance, validated_data):
        sourceType_data = validated_data.pop('sourceType')
        if sourceType_data:
            sourceType = SourceType.objects.get_or_create(id=sourceType_data['id'])[0]
            validated_data['sourceType'] = sourceType
        client_data = validated_data.pop('client')
        if client_data:
            client = Client.objects.get_or_create(id=client_data['id'])[0]
            validated_data['client'] = client
        company_data = validated_data.pop('company')
        if company_data:
            company = Company.objects.get_or_create(id=company_data['id'])[0]
            validated_data['company'] = company

        instance.code = validated_data.get('code', instance.code)
        instance.description = validated_data.get('description', instance.description)
        instance.sourceType = validated_data.get('sourceType', instance.sourceType)
        instance.date_start = validated_data.get('date_start', instance.date_start)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.status = validated_data.get('status', instance.status)
        instance.client = validated_data.get('client', instance.client)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance
