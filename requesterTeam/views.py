from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from requesterTeam.models import RequesterTeam
from requesterTeam.serializers import RequesterTeamSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def requester_team_list(request):
    if request.method == 'GET':
        requester_team = RequesterTeam.objects.all()
        requester_team_serializer = RequesterTeamSerializer(requester_team, many=True)
        return JsonResponse(requester_team_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        requester_team_data = JSONParser().parse(request)
        requester_team_serializer = RequesterTeamSerializer(data=requester_team_data)
        if requester_team_serializer.is_valid():
            requester_team_serializer.save()
            return JsonResponse(requester_team_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(requester_team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        RequesterTeam.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def requester_team_detail(request, pk):
    try:
        requester_team = RequesterTeam.objects.get(pk=pk)
    except RequesterTeam.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        requester_team_serializer = RequesterTeamSerializer(requester_team)
        return JsonResponse(requester_team_serializer.data)

    elif request.method == 'PUT':
        requester_team_data = JSONParser().parse(request)
        requester_team_serializer = RequesterTeamSerializer(requester_team, data=requester_team_data)
        if requester_team_serializer.is_valid():
            requester_team_serializer.save()
            return JsonResponse(requester_team_serializer.data)
        return JsonResponse(requester_team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        requester_team.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def requester_team_list_id(request, id):
    requester_team = RequesterTeam.objects.filter(id=id)

    if request.method == 'GET':
        requester_team_serializer = RequesterTeamSerializer(requester_team, many=True)
        return JsonResponse(requester_team_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'