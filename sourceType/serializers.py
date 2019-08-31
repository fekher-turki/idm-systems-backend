from rest_framework import serializers
from sourceType.models import SourceType


class SourceTypeSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=SourceType._meta.get_field('id'), required=False)

    class Meta:
        model = SourceType
        extra_kwargs = {
            'code': {'validators': []},
        }
        fields = ('id',
                  'code',
                  'name',
                  'description',
                  'created_at',
                  'updated_at')
