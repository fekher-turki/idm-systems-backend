from rest_framework import serializers

from source.models import Source
from source.serializers import SourceSerializer
from sourceTeam.models import SourceTeam
from team.models import Team
from team.serializers import TeamSerializer


class SourceTeamSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=SourceTeam._meta.get_field('id'), required=False)
    source = SourceSerializer(many=False)
    team = TeamSerializer(many=False)

    class Meta:
        model = SourceTeam
        extra_kwargs = {
            'id': {'validators': []},
        }
        fields = ('id',
                  'source',
                  'team',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        source_data = validated_data.pop('source')
        if source_data:
            source = Source.objects.get_or_create(id=source_data['id'])[0]
            validated_data['source'] = source
        team_data = validated_data.pop('team')
        if team_data:
            team = Team.objects.get_or_create(id=team_data['id'])[0]
            validated_data['team'] = team
        return SourceTeam.objects.create(**validated_data)

    def update(self, instance, validated_data):
        source_data = validated_data.pop('source')
        if source_data:
            source = Source.objects.get_or_create(id=source_data['id'])[0]
            validated_data['source'] = source
        team_data = validated_data.pop('team')
        if team_data:
            team = Team.objects.get_or_create(id=team_data['id'])[0]
            validated_data['team'] = team
        instance.source = validated_data.get('source', instance.source)
        instance.team = validated_data.get('team', instance.team)
        instance.save()
        return instance
