from rest_framework import serializers
from team.models import Team


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Team._meta.get_field('id'), required=False)

    class Meta:
        model = Team
        extra_kwargs = {
            'id': {'validators': []},
            'code': {'validators': []},
        }
        fields = ('id',
                  'code',
                  'description',
                  'created_at',
                  'updated_at')
