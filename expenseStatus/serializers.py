from rest_framework import serializers

from approver.models import Approver
from approver.serializers import ApproverSerializer
from expenseStatus.models import ExpenseStatus


class ExpenseStatusSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=ExpenseStatus._meta.get_field('id'), required=False)
    approver = ApproverSerializer(many=False)

    class Meta:
        model = ExpenseStatus
        unique_together = ('approver', 'expense',)
        fields = ('id',
                  'approver',
                  'expense',
                  'status',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        approver_data = validated_data.pop('approver')
        if approver_data:
            approver = Approver.objects.get_or_create(id=approver_data['id'])[0]
            validated_data['approver'] = approver
        return ExpenseStatus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        approver_data = validated_data.pop('approver')
        if approver_data:
            approver = Approver.objects.get_or_create(id=approver_data['id'])[0]
            validated_data['approver'] = approver
        instance.approver = validated_data.get('approver', instance.approver)
        instance.expense = validated_data.get('expense', instance.expense)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
