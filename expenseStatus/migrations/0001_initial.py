# Generated by Django 2.2.1 on 2019-08-31 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('approver', '0001_initial'),
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenseStatus_approver', to='approver.Approver')),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenseStatus_expense', to='expense.Expense')),
            ],
            options={
                'unique_together': {('approver', 'expense')},
            },
        ),
    ]
