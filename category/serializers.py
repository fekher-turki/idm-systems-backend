from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Category._meta.get_field('id'), required=False)

    class Meta:
        model = Category
        extra_kwargs = {
            'accounting_code': {'validators': []},
        }
        fields = ('id',
                  'accounting_code',
                  'name',
                  'description',
                  'created_at',
                  'updated_at')
