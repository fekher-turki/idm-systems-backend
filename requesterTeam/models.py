from django.db import models

from requester.models import Requester
from team.models import Team


class RequesterTeam(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='requesterTeam_team')
    requester = models.ForeignKey(Requester, on_delete=models.CASCADE, related_name='requesterTeam_requester')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('team', 'requester',)

    def __int__(self):
        return self.id
