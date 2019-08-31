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
from expenseReport.models import ExpenseReport
from expenseReport.serializers import ExpenseReportSerializer
from requester.models import Requester
from requesterTeam.models import RequesterTeam
from team.models import Team


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseReport_list(request):
    if request.method == 'GET':
        expenseReport = ExpenseReport.objects.all()
        expenseReport_serializer = ExpenseReportSerializer(expenseReport, many=True)
        return JsonResponse(expenseReport_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        expenseReport_data = JSONParser().parse(request)
        expenseReport_serializer = ExpenseReportSerializer(data=expenseReport_data)
        if expenseReport_serializer.is_valid():
            if expenseReport_data['date_start'] > expenseReport_data['date_end']:
                return JsonResponse(expenseReport_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            expenseReport_serializer.save()
            return JsonResponse(expenseReport_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(expenseReport_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ExpenseReport.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseReport_detail(request, pk):
    try:
        expenseReport = ExpenseReport.objects.get(pk=pk)
    except ExpenseReport.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        expenseReport_serializer = ExpenseReportSerializer(expenseReport)
        return JsonResponse(expenseReport_serializer.data)

    elif request.method == 'PUT':
        expenseReport_data = JSONParser().parse(request)
        expenseReport_serializer = ExpenseReportSerializer(expenseReport, data=expenseReport_data)
        if expenseReport_serializer.is_valid():
            expenseReport_serializer.save()
            return JsonResponse(expenseReport_serializer.data)
        return JsonResponse(expenseReport_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        expenseReport.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def countExpenseReport(request):
    if request.method == 'GET':
        expenseReport = ExpenseReport.objects.count()
        count = [expenseReport]
        return JsonResponse(count, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseReport_list_id(request, id):
    expenseReport = ExpenseReport.objects.filter(id=id)

    if request.method == 'GET':
        expenseReport_serializer = ExpenseReportSerializer(expenseReport, many=True)
        return JsonResponse(expenseReport_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseReport_count(request, id):
    if request.method == 'GET':
        expenseReport = ExpenseReport.objects.filter(id=id)
        requesterTeam = RequesterTeam.objects.filter(expenseReport_requesterTeam=expenseReport[0])
        team = Team.objects.filter(requesterTeam_team=requesterTeam[0])
        approvers = ApproverTeam.objects.filter(team=team[0]).count()
        count = [approvers]
        return JsonResponse(count, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseReport_list_user(request, user):
    employee = Employee.objects.filter(user_id=user)
    requester = Requester.objects.filter(employee=employee[0])
    requesterTeam = RequesterTeam.objects.filter(requester=requester[0])
    expenseReport = ExpenseReport.objects.filter(requesterTeam=requesterTeam[0])

    if request.method == 'GET':
        expenseReport_serializer = ExpenseReportSerializer(expenseReport, many=True)
        return JsonResponse(expenseReport_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseReport_detail_mod(request, id, mod):
    expenseReportList = []
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
                        expenseReports = ExpenseReport.objects.filter(id=id, requesterTeam=requesterTeam)
                        for expenseReport in expenseReports:
                            expenseReportList.append(expenseReport)
    if request.method == 'GET':
        expenseReport_serializer = ExpenseReportSerializer(expenseReportList, many=True)
        return JsonResponse(expenseReport_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseReport_list_mod(request, mod):
    expenseReportList = []
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
                            expenseReportList.append(expenseReport)
    if request.method == 'GET':
        expenseReport_serializer = ExpenseReportSerializer(expenseReportList, many=True)
        return JsonResponse(expenseReport_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def expenseReport_detail_user(request, user, id):
    employee = Employee.objects.filter(user_id=user)
    requester = Requester.objects.filter(employee=employee[0])
    requesterTeam = RequesterTeam.objects.filter(requester=requester[0])
    expenseReport = ExpenseReport.objects.filter(id=id, requesterTeam=requesterTeam[0])

    if request.method == 'GET':
        expenseReport_serializer = ExpenseReportSerializer(expenseReport, many=True)
        return JsonResponse(expenseReport_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
