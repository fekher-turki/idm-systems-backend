from rest_framework import serializers
from rule.models import Rule


class RuleSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Rule._meta.get_field('id'), required=False)

    class Meta:
        model = Rule
        extra_kwargs = {
            'code': {'validators': []},
        }
        fields = ('id',
                  'description',
                  'value',
                  'created_at',
                  'updated_at')
