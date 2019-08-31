from rest_framework import serializers

from category.models import Category
from category.serializers import CategorySerializer
from currency.models import Currency
from currency.serializers import CurrencySerializer
from exchangeRate.serializers import ExchangeRateSerializer
from expense.models import Expense
from expenseReport.models import ExpenseReport
from expenseReport.serializers import ExpenseReportSerializer


class ExpenseSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Expense._meta.get_field('id'), required=False)
    expenseReport = ExpenseReportSerializer(many=False)
    category = CategorySerializer(many=False)
    currency = CurrencySerializer(many=False)
    exchangeRate = ExchangeRateSerializer(many=False, required=False)
    image = serializers.ImageField(use_url=True, max_length=2621440)

    class Meta:
        model = Expense
        extra_kwargs = {
            'reference': {'validators': []},
        }
        fields = ('id',
                  'reference',
                  'expenseReport',
                  'date',
                  'image',
                  'category',
                  'description',
                  'amount_ini',
                  'amount_final',
                  'currency',
                  'exchangeRate',
                  'draft',
                  'status',
                  'created_at',
                  'updated_at')

    def create(self, validated_data):
        expenseReport_data = validated_data.pop('expenseReport')
        if expenseReport_data:
            expenseReport = ExpenseReport.objects.get_or_create(id=expenseReport_data['id'])[0]
            validated_data['expenseReport'] = expenseReport
        category_data = validated_data.pop('category')
        if category_data:
            category = Category.objects.get_or_create(id=category_data['id'])[0]
            validated_data['category'] = category
        currency_data = validated_data.pop('currency')
        if currency_data:
            currency = Currency.objects.get_or_create(id=currency_data['id'])[0]
            validated_data['currency'] = currency
        return Expense.objects.create(**validated_data)

    def update(self, instance, validated_data):
        expenseReport_data = validated_data.pop('expenseReport')
        if expenseReport_data:
            expenseReport = ExpenseReport.objects.get_or_create(id=expenseReport_data['id'])[0]
            validated_data['expenseReport'] = expenseReport
        category_data = validated_data.pop('category')
        if category_data:
            category = Category.objects.get_or_create(id=category_data['id'])[0]
            validated_data['category'] = category
        currency_data = validated_data.pop('currency')
        if currency_data:
            currency = Currency.objects.get_or_create(id=currency_data['id'])[0]
            validated_data['currency'] = currency
        instance.reference = validated_data.get('reference', instance.reference)
        instance.expenseReport = validated_data.get('expenseReport', instance.expenseReport)
        instance.date = validated_data.get('date', instance.date)
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        instance.amount_ini = validated_data.get('amount_ini', instance.amount_ini)
        instance.amount_final = validated_data.get('amount_final', instance.amount_final)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.exchangeRate = validated_data.get('exchangeRate', instance.exchangeRate)
        instance.draft = validated_data.get('draft', instance.draft)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
