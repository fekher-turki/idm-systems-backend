from django.db import models

from source.models import Source
from team.models import Team


class SourceTeam(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='sourceTeam_source')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='sourceTeam_team')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('source', 'team',)

    def __int__(self):
        return self.id
