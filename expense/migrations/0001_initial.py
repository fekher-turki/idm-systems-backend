# Generated by Django 2.2.1 on 2019-08-31 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('expenseReport', '0001_initial'),
        ('category', '0001_initial'),
        ('exchangeRate', '0001_initial'),
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reference', models.CharField(default='', max_length=12)),
                ('date', models.DateField(default='')),
                ('image', models.ImageField(blank=True, default='', max_length=2621440, upload_to='expense/')),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('amount_ini', models.FloatField(default=0)),
                ('amount_final', models.FloatField(default=0)),
                ('draft', models.BooleanField(blank=True, default=0)),
                ('status', models.BooleanField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_category', to='category.Category')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_currency', to='currency.Currency')),
                ('exchangeRate', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='expense_exchangeRate', to='exchangeRate.ExchangeRate')),
                ('expenseReport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_expenseReport', to='expenseReport.ExpenseReport')),
            ],
        ),
    ]
