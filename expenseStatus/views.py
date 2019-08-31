from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from approver.models import Approver
from approverTeam.models import ApproverTeam
from employee.models import Employee
from expense.models import Expense
from expenseReport.models import ExpenseReport
from expenseStatus.models import ExpenseStatus
from expenseStatus.serializers import ExpenseStatusSerializer
from requesterTeam.models import RequesterTeam
from rule.models import Rule
from team.models import Team


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseStatus_list(request):
    if request.method == 'GET':
        expenseStatus = ExpenseStatus.objects.all()
        expenseStatus_serializer = ExpenseStatusSerializer(expenseStatus, many=True)
        return JsonResponse(expenseStatus_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        expenseStatus_data = JSONParser().parse(request)
        approver_ = expenseStatus_data['approver']['id']
        expense_ = expenseStatus_data['expense']
        if ExpenseStatus.objects.filter(expense_id=expense_, approver_id=approver_):
            return JsonResponse('Already exist !', status=status.HTTP_400_BAD_REQUEST, safe=False)
        status_input = expenseStatus_data['status']
        expense_id = expenseStatus_data['expense']
        expense = Expense.objects.filter(id=expense_id)
        # expenseStatus for counting existing decides
        expenseStatus = ExpenseStatus.objects.filter(expense=expense[0]).filter(status=True).count()

        # approversTeam for counting number of deciders
        expenseReport = ExpenseReport.objects.filter(expense_expenseReport=expense[0])

        # getting the rule
        rules = Rule.objects.filter(expenseReport_rule=expenseReport[0])
        rule = rules[0].value
        ###########

        requesterTeam = RequesterTeam.objects.filter(expenseReport_requesterTeam=expenseReport[0])
        team = Team.objects.filter(requesterTeam_team=requesterTeam[0])
        approversTeam = ApproverTeam.objects.filter(team=team[0]).count()
        ##########################
        expenseStatus_serializer = ExpenseStatusSerializer(data=expenseStatus_data)

        if expenseStatus_serializer.is_valid():
            expenseStatus_serializer.save()
            if status_input:
                expenseStatus += 1
            decided = ((expenseStatus / approversTeam) * 100)
            if (decided - rule) >= 0:
                Expense.objects.filter(id=expense_id).update(status=True)
            return JsonResponse(expenseStatus_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(expenseStatus_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ExpenseStatus.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseStatus_detail(request, pk):
    try:
        expenseStatus = ExpenseStatus.objects.get(pk=pk)
    except ExpenseStatus.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        expenseStatus_serializer = ExpenseStatusSerializer(expenseStatus)
        return JsonResponse(expenseStatus_serializer.data)

    elif request.method == 'PUT':
        expenseStatus_data = JSONParser().parse(request)
        expenseStatus_serializer = ExpenseStatusSerializer(expenseStatus, data=expenseStatus_data)
        if expenseStatus_serializer.is_valid():
            expenseStatus_serializer.save()
            return JsonResponse(expenseStatus_serializer.data)
        return JsonResponse(expenseStatus_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        expenseStatus.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseStatus_list_id(request, id):
    expenseStatus = ExpenseStatus.objects.filter(id=id)

    if request.method == 'GET':
        expenseStatus_serializer = ExpenseStatusSerializer(expenseStatus, many=True)
        return JsonResponse(expenseStatus_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseStatus_list_expense(request, expense):
    expenseStatus = ExpenseStatus.objects.filter(expense=expense)

    if request.method == 'GET':
        expenseStatus_serializer = ExpenseStatusSerializer(expenseStatus, many=True)
        return JsonResponse(expenseStatus_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseStatus_list_count(request, expense):
    if request.method == 'GET':
        expenseStatus = ExpenseStatus.objects.filter(expense=expense).count()
        count = [expenseStatus, ]
        return JsonResponse(count, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseStatus_mod_expense(request, mod, expense):
    employee = Employee.objects.filter(user=mod)
    approver = Approver.objects.filter(employee=employee)
    expenseStatus = ExpenseStatus.objects.filter(approver=approver, expense_id=expense)

    if request.method == 'GET':
        expenseStatus_serializer = ExpenseStatusSerializer(expenseStatus, many=True)
        return JsonResponse(expenseStatus_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'