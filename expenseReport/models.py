from django.db import models

from requesterTeam.models import RequesterTeam
from rule.models import Rule
from sourceTeam.models import SourceTeam


class ExpenseReport(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=12, blank=False, unique=True, default='')
    requesterTeam = models.ForeignKey(RequesterTeam, on_delete=models.CASCADE, related_name='expenseReport_requesterTeam')
    date_start = models.DateField(blank=False, default='')
    date_end = models.DateField(blank=False, default='')
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, blank=False, related_name='expenseReport_rule')
    sourceTeam = models.OneToOneField(SourceTeam, on_delete=models.CASCADE, blank=False, related_name='expenseReport_sourceTeam')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
