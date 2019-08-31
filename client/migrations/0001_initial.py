# Generated by Django 2.2.1 on 2019-08-31 17:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
        ('clientType', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(999)])),
                ('name', models.CharField(max_length=70)),
                ('fiscal_number', models.CharField(blank=True, default='', max_length=100)),
                ('vat_number', models.CharField(blank=True, default='', max_length=100)),
                ('tel_number', models.IntegerField(blank=True, default=0)),
                ('email', models.EmailField(default='', max_length=254)),
                ('address1', models.CharField(blank=True, default='', max_length=100)),
                ('address2', models.CharField(blank=True, default='', max_length=100)),
                ('zip_code', models.CharField(blank=True, default='', max_length=10)),
                ('city', models.CharField(blank=True, default='', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clientType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_clientType', to='clientType.ClientType')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_country', to='country.Country')),
            ],
        ),
    ]
