# Generated by Django 2.2.1 on 2019-08-31 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        ('source', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sourceTeam_source', to='source.Source')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sourceTeam_team', to='team.Team')),
            ],
            options={
                'unique_together': {('source', 'team')},
            },
        ),
    ]
