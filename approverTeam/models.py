from django.db import models

from approver.models import Approver
from team.models import Team


class ApproverTeam(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='approverTeam_team')
    approver = models.ForeignKey(Approver, on_delete=models.CASCADE, related_name='approverTeam_approver')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('team', 'approver',)

    def __int__(self):
        return self.id
