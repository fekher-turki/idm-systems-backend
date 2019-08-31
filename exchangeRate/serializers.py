from rest_framework import serializers

from currency.models import Currency
from currency.serializers import CurrencySerializer
from exchangeRate.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=ExchangeRate._meta.get_field('id'), required=False)
    currency = CurrencySerializer(many=False)

    class Meta:
        model = ExchangeRate
        fields = ('id',
                  'currency',
                  'value',
                  'date',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        currency_data = validated_data.pop('currency')
        if currency_data:
            currency = Currency.objects.get_or_create(id=currency_data['id'])[0]
            validated_data['currency'] = currency
        return ExchangeRate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        currency_data = validated_data.pop('currency')
        if currency_data:
            currency = Currency.objects.get_or_create(id=currency_data['id'])[0]
            validated_data['currency'] = currency
        instance.currency = validated_data.get('currency', instance.currency)
        instance.value = validated_data.get('value', instance.value)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
