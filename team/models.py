from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=8, unique=True, blank=True, default='')
    description = models.CharField(max_length=70, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
