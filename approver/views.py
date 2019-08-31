from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from approver.models import Approver
from approver.serializers import ApproverSerializer
from employee.models import Employee


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def approver_list(request):
    if request.method == 'GET':
        approver = Approver.objects.all()
        approver_serializer = ApproverSerializer(approver, many=True)
        return JsonResponse(approver_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        approver_data = JSONParser().parse(request)
        approver_serializer = ApproverSerializer(data=approver_data)
        if approver_serializer.is_valid():
            approver_serializer.save()
            return JsonResponse(approver_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(approver_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Approver.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def approver_detail(request, pk):
    try:
        approver = Approver.objects.get(pk=pk)
    except Approver.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        approver_serializer = ApproverSerializer(approver)
        return JsonResponse(approver_serializer.data)

    elif request.method == 'PUT':
        approver_data = JSONParser().parse(request)
        approver_serializer = ApproverSerializer(approver, data=approver_data)
        if approver_serializer.is_valid():
            approver_serializer.save()
            return JsonResponse(approver_serializer.data)
        return JsonResponse(approver_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        approver.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def approver_list_id(request, id):
    approver = Approver.objects.filter(id=id)

    if request.method == 'GET':
        approver_serializer = ApproverSerializer(approver, many=True)
        return JsonResponse(approver_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def approver_list_user(request, user):
    employee = Employee.objects.filter(user_id=user)
    approver = Approver.objects.filter(employee=employee[0])

    if request.method == 'GET':
        approver_serializer = ApproverSerializer(approver, many=True)
        return JsonResponse(approver_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'