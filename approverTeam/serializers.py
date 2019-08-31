from rest_framework import serializers

from approver.models import Approver
from approver.serializers import ApproverSerializer
from approverTeam.models import ApproverTeam
from team.models import Team
from team.serializers import TeamSerializer


class ApproverTeamSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=ApproverTeam._meta.get_field('id'), required=False)
    team = TeamSerializer(many=False)
    approver = ApproverSerializer(many=False)

    class Meta:
        model = ApproverTeam
        fields = ('id',
                  'team',
                  'approver',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        team_data = validated_data.pop('team')
        if team_data:
            team = Team.objects.get_or_create(id=team_data['id'])[0]
            validated_data['team'] = team
        approver_data = validated_data.pop('approver')
        if approver_data:
            approver = Approver.objects.get_or_create(id=approver_data['id'])[0]
            validated_data['approver'] = approver
        return ApproverTeam.objects.create(**validated_data)

    def update(self, instance, validated_data):
        team_data = validated_data.pop('team')
        if team_data:
            team = Team.objects.get_or_create(id=team_data['id'])[0]
            validated_data['team'] = team
        approver_data = validated_data.pop('approver')
        if approver_data:
            approver = Approver.objects.get_or_create(id=approver_data['id'])[0]
            validated_data['approver'] = approver
        instance.team = validated_data.get('team', instance.team)
        instance.approver = validated_data.get('approver', instance.approver)
        instance.save()
        return instance
