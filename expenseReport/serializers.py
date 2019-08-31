from rest_framework import serializers
from expenseReport.models import ExpenseReport
from requesterTeam.models import RequesterTeam
from requesterTeam.serializers import RequesterTeamSerializer
from rule.models import Rule
from rule.serializers import RuleSerializer
from sourceTeam.models import SourceTeam
from sourceTeam.serializers import SourceTeamSerializer


class ExpenseReportSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=ExpenseReport._meta.get_field('id'), required=False)
    requesterTeam = RequesterTeamSerializer(many=False)
    rule = RuleSerializer(many=False)
    sourceTeam = SourceTeamSerializer(many=False)

    class Meta:
        model = ExpenseReport
        extra_kwargs = {
            'reference': {'validators': []},
        }
        fields = ('id',
                  'reference',
                  'requesterTeam',
                  'date_start',
                  'date_end',
                  'rule',
                  'sourceTeam',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        requesterTeam_data = validated_data.pop('requesterTeam')
        if requesterTeam_data:
            requesterTeam = RequesterTeam.objects.get_or_create(id=requesterTeam_data['id'])[0]
            validated_data['requesterTeam'] = requesterTeam
        rule_data = validated_data.pop('rule')
        if rule_data:
            rule = Rule.objects.get_or_create(id=rule_data['id'])[0]
            validated_data['rule'] = rule
        sourceTeam_data = validated_data.pop('sourceTeam')
        if sourceTeam_data:
            sourceTeam = SourceTeam.objects.get_or_create(id=sourceTeam_data['id'])[0]
            validated_data['sourceTeam'] = sourceTeam
        return ExpenseReport.objects.create(**validated_data)

    def update(self, instance, validated_data):
        requesterTeam_data = validated_data.pop('requesterTeam')
        if requesterTeam_data:
            requesterTeam = RequesterTeam.objects.get_or_create(id=requesterTeam_data['id'])[0]
            validated_data['requesterTeam'] = requesterTeam
        rule_data = validated_data.pop('rule')
        if rule_data:
            rule = Rule.objects.get_or_create(id=rule_data['id'])[0]
            validated_data['rule'] = rule
        sourceTeam_data = validated_data.pop('sourceTeam')
        if sourceTeam_data:
            sourceTeam = SourceTeam.objects.get_or_create(id=sourceTeam_data['id'])[0]
            validated_data['sourceTeam'] = sourceTeam
        instance.reference = validated_data.get('reference', instance.reference)
        instance.requesterTeam = validated_data.get('requesterTeam', instance.requesterTeam)
        instance.date_start = validated_data.get('date_start', instance.date_start)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.rule = validated_data.get('rule', instance.rule)
        instance.sourceTeam = validated_data.get('sourceTeam', instance.sourceTeam)
        instance.save()
        return instance
