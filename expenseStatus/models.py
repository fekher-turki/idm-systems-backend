from django.db import models

from approver.models import Approver
from expense.models import Expense


class ExpenseStatus(models.Model):
    id = models.AutoField(primary_key=True)
    approver = models.ForeignKey(Approver, on_delete=models.CASCADE, related_name='expenseStatus_approver')
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='expenseStatus_expense')
    status = models.IntegerField(blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('approver', 'expense',)

    def __int__(self):
        return self.id
