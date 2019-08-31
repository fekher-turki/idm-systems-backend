from rest_framework import serializers
from clientType.models import ClientType


class ClientTypeSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=ClientType._meta.get_field('id'), required=False)

    class Meta:
        model = ClientType
        extra_kwargs = {
            'code': {'validators': []},
        }
        fields = ('id',
                  'code',
                  'name',
                  'description',
                  'created_at',
                  'updated_at')
