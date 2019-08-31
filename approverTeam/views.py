from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from approverTeam.models import ApproverTeam
from approverTeam.serializers import ApproverTeamSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def approver_team_list(request):
    if request.method == 'GET':
        approver_team = ApproverTeam.objects.all()
        approver_team_serializer = ApproverTeamSerializer(approver_team, many=True)
        return JsonResponse(approver_team_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        approver_team_data = JSONParser().parse(request)
        approver_team_serializer = ApproverTeamSerializer(data=approver_team_data)
        if approver_team_serializer.is_valid():
            approver_team_serializer.save()
            return JsonResponse(approver_team_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(approver_team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ApproverTeam.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def approver_team_detail(request, pk):
    try:
        approver_team = ApproverTeam.objects.get(pk=pk)
    except ApproverTeam.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        approver_team_serializer = ApproverTeamSerializer(approver_team)
        return JsonResponse(approver_team_serializer.data)

    elif request.method == 'PUT':
        approver_team_data = JSONParser().parse(request)
        approver_team_serializer = ApproverTeamSerializer(approver_team, data=approver_team_data)
        if approver_team_serializer.is_valid():
            approver_team_serializer.save()
            return JsonResponse(approver_team_serializer.data)
        return JsonResponse(approver_team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        approver_team.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def approver_team_list_id(request, id):
    approver_team = ApproverTeam.objects.filter(id=id)

    if request.method == 'GET':
        approver_team_serializer = ApproverTeamSerializer(approver_team, many=True)
        return JsonResponse(approver_team_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'