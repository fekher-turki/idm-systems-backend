from rest_framework import serializers

from requester.models import Requester
from requester.serializers import RequesterSerializer
from requesterTeam.models import RequesterTeam
from team.models import Team
from team.serializers import TeamSerializer


class RequesterTeamSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=RequesterTeam._meta.get_field('id'), required=False)
    team = TeamSerializer(many=False)
    requester = RequesterSerializer(many=False)

    class Meta:
        model = RequesterTeam
        fields = ('id',
                  'team',
                  'requester',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        team_data = validated_data.pop('team')
        if team_data:
            team = Team.objects.get_or_create(id=team_data['id'])[0]
            validated_data['team'] = team
        requester_data = validated_data.pop('requester')
        if requester_data:
            requester = Requester.objects.get_or_create(id=requester_data['id'])[0]
            validated_data['requester'] = requester
        return RequesterTeam.objects.create(**validated_data)

    def update(self, instance, validated_data):
        team_data = validated_data.pop('team')
        if team_data:
            team = Team.objects.get_or_create(id=team_data['id'])[0]
            validated_data['team'] = team
        requester_data = validated_data.pop('requester')
        if requester_data:
            requester = Requester.objects.get_or_create(id=requester_data['id'])[0]
            validated_data['requester'] = requester
        instance.team = validated_data.get('team', instance.team)
        instance.requester = validated_data.get('requester', instance.requester)
        instance.save()
        return instance
