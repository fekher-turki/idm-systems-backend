from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException
from django.db import models
from rest_framework.response import Response

from category.models import Category
from currency.models import Currency
from exchangeRate.models import ExchangeRate
from expenseReport.models import ExpenseReport
from datetime import date as today_date


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=12, blank=False, default='')
    expenseReport = models.ForeignKey(ExpenseReport, blank=False, on_delete=models.CASCADE, related_name='expense_expenseReport')
    date = models.DateField(blank=False, default='')
    image = models.ImageField(upload_to='expense/', blank=True, max_length=2621440, default='')
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE, related_name='expense_category')
    description = models.CharField(max_length=255, blank=True, default='')
    amount_ini = models.FloatField(blank=False, default=0)
    amount_final = models.FloatField(blank=False, default=0)
    currency = models.ForeignKey(Currency, blank=False, on_delete=models.CASCADE, related_name='expense_currency')
    exchangeRate = models.ForeignKey(ExchangeRate, blank=True, on_delete=models.CASCADE, related_name='expense_exchangeRate')
    draft = models.BooleanField(blank=True, default=0)
    status = models.BooleanField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self.date < self.expenseReport.date_start:
            raise ValidationError({'error': 'The date cannot be before Expense note !', 'status': 'HTTP_400_BAD_REQUEST'})
        if self.date > self.expenseReport.date_end:
            raise ValidationError({'error': 'The date cannot be after Expense note !', 'status': 'HTTP_400_BAD_REQUEST'})
        if self.date > today_date.today():
            raise ValidationError({'error': 'Are you from the future ? check your date !', 'status': 'HTTP_400_BAD_REQUEST'})
        # initializing amount final value
        self.amount_final = 0.0
        date = self.date
        # getting exchange rate from current currency
        y = ExchangeRate.objects.filter(currency=self.currency)
        # getting closest exchange rate filtered by date
        dates = []
        for x in y:
            dates += [x.date]
        closest_date = min(dates, key=lambda d: abs(d - date))
        # getting exchange rate from current currency and have closest date to expense's date
        exchange_rate = ExchangeRate.objects.filter(currency=self.currency).filter(date=closest_date)
        # affecting exchange to current expense's currency
        self.exchangeRate = exchange_rate[0]
        # setting the decimal place for the expense's amount
        amount_ini = round(self.amount_ini, self.currency.decimal_place)
        self.amount_ini = amount_ini
        # calculating the final amount: amount initial * exchange rate value (with decimal place of exchange rate)
        self.amount_final = round((float(amount_ini) * float(exchange_rate[0].value)), self.currency.decimal_place)
        super(Expense, self).save(*args, **kwargs)
