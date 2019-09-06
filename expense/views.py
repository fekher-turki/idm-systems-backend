from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import parser_classes, api_view, authentication_classes, permission_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.utils import json

from approver.models import Approver
from approverTeam.models import ApproverTeam
from employee.models import Employee
from expense.models import Expense
from expense.serializers import ExpenseSerializer
from expenseReport.models import ExpenseReport
from requester.models import Requester
from requesterTeam.models import RequesterTeam
from team.models import Team


@parser_classes([FormParser, MultiPartParser])
@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expense_list(request):
    if request.method == 'GET':
        expense = Expense.objects.all()
        expense_serializer = ExpenseSerializer(expense, many=True)
        return JsonResponse(expense_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        draft = request.POST.get('draft')
        try:
            draft_data = (int(draft))
        except:
            draft_data = 1
        reference = request.POST.get('reference')
        expenseReport = request.POST.get('expenseReport')
        expenseReport_data = json.loads(expenseReport)
        date = request.POST.get('date')
        category = request.POST.get('category')
        category_data = json.loads(category)
        description = request.POST.get('description')
        amount_ini = request.POST.get('amount_ini')
        currency = request.POST.get('currency')
        currency_data = json.loads(currency)
        try:
            image_data = request.FILES['image']
        except KeyError:
            return JsonResponse(
                'Upload a valid image. The file you uploaded was either not an image or a corrupted image',
                status=status.HTTP_400_BAD_REQUEST)
        expense_data = {"reference": reference, "expenseReport": expenseReport_data, "date": date,
                        "category": category_data, "description": description, "amount_ini": float(amount_ini),
                        "currency": currency_data, "draft": draft_data, 'image': image_data}
        expense_serializer = ExpenseSerializer(data=expense_data)
        if expense_serializer.is_valid():
            expense_serializer.save()
            return JsonResponse(expense_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(expense_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     Expense.objects.all().delete()
    #     return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@parser_classes([FormParser, MultiPartParser])
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expense_detail(request, pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        expense_serializer = ExpenseSerializer(expense)
        return JsonResponse(expense_serializer.data)

    elif request.method == 'PUT':
        request.method = "POST"
        draft = request.POST.get('draft')
        expense_ = Expense.objects.filter(id=request.POST.get('id'))
        status = expense_[0].status
        if status:
            return HttpResponse('Already decided !')
        try:
            draft_data = (int(draft))
        except:
            draft_data = 1
        reference = request.POST.get('reference')
        expenseReport = request.POST.get('expenseReport')
        expenseReport_data = json.loads(expenseReport)
        date = request.POST.get('date')
        category = request.POST.get('category')
        category_data = json.loads(category)
        description = request.POST.get('description')
        amount_ini = request.POST.get('amount_ini')
        currency = request.POST.get('currency')
        currency_data = json.loads(currency)
        if not dict(request.FILES):
            expense = Expense.objects.get(pk=pk)
            image_data = expense.image
        else:
            image_data = request.FILES['image']
        if draft_data is None:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        expense_data = {"reference": reference, "expenseReport": expenseReport_data, "date": date,
                        "category": category_data, "description": description, "amount_ini": float(amount_ini),
                        "currency": currency_data, "draft": draft_data, 'image': image_data}
        expense_serializer = ExpenseSerializer(expense, data=expense_data)
        if expense_serializer.is_valid():
            expense_serializer.save()
            return JsonResponse(expense_serializer.data)
        return JsonResponse(expense_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if expense.status:
            return HttpResponse('Already decided !')
        expense.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def countExpense(request):
    if request.method == 'GET':
        expense = Expense.objects.count()
        count = [expense]
        return JsonResponse(count, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expense_list_id(request, id):
    expense = Expense.objects.filter(id=id)

    if request.method == 'GET':
        expense_serializer = ExpenseSerializer(expense, many=True)
        return JsonResponse(expense_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expense_list_expense_report(request, expenseReport):
    expense = Expense.objects.filter(expenseReport=expenseReport)

    if request.method == 'GET':
        expense_serializer = ExpenseSerializer(expense, many=True)
        return JsonResponse(expense_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def user_expense_list(request, user):
    if request.method == 'GET':
        employee = Employee.objects.filter(user_id=user)
        requester = Requester.objects.filter(employee=employee[0])
        requesterTeam = RequesterTeam.objects.filter(requester=requester[0])
        expenseReport = ExpenseReport.objects.filter(requesterTeam=requesterTeam[0])
        expense = Expense.objects.filter(expenseReport=expenseReport[0])
        expense_serializer = ExpenseSerializer(expense, many=True)
        return JsonResponse(expense_serializer.data, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expense_detail_user(request, user, id):
    if request.method == 'GET':
        employee = Employee.objects.filter(user_id=user)
        requester = Requester.objects.filter(employee=employee[0])
        requesterTeam = RequesterTeam.objects.filter(requester=requester[0])
        expenseReport = ExpenseReport.objects.filter(requesterTeam=requesterTeam[0])
        expense = Expense.objects.filter(id=id, expenseReport=expenseReport[0])
        expense_serializer = ExpenseSerializer(expense, many=True)
        return JsonResponse(expense_serializer.data, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def mod_expense_list_expense_report(request, mod, expenseReport_):
    if request.method == 'GET':
        expenseList = []
        employees = Employee.objects.filter(user_id=mod)
        for employee in employees:
            approvers = Approver.objects.filter(employee=employee)
            for approver in approvers:
                approverTeams = ApproverTeam.objects.filter(approver=approver)
                for approverTeam in approverTeams:
                    teams = Team.objects.filter(approverTeam_team=approverTeam)
                    for team in teams:
                        requesterTeams = RequesterTeam.objects.filter(team=team)
                        for requesterTeam in requesterTeams:
                            expenseReports = ExpenseReport.objects.filter(requesterTeam=requesterTeam)
                            for expenseReport in expenseReports:
                                expenses = Expense.objects.filter(expenseReport=expenseReport).filter(expenseReport=expenseReport_)
                                for expense in expenses:
                                    expenseList.append(expense)
        expenseReport_serializer = ExpenseSerializer(expenseList, many=True)
        return JsonResponse(expenseReport_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'