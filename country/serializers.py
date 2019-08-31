from rest_framework import serializers
from country.models import Country


class CountrySerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Country._meta.get_field('id'), required=False)

    class Meta:
        model = Country
        extra_kwargs = {
            'code': {'validators': []},
        }
        fields = ('id',
                  'code',
                  'name',
                  'created_at',
                  'updated_at')
