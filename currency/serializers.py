from rest_framework import serializers
from currency.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Currency._meta.get_field('id'), required=False)

    class Meta:
        model = Currency
        extra_kwargs = {
            'code': {'validators': []},
        }
        fields = ('id',
                  'code',
                  'description',
                  'decimal_place',
                  'symbol',
                  'created_at',
                  'updated_at')
