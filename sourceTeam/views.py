from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from sourceTeam.models import SourceTeam
from sourceTeam.serializers import SourceTeamSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def source_team_list(request):
    if request.method == 'GET':
        source_team = SourceTeam.objects.all()
        source_team_serializer = SourceTeamSerializer(source_team, many=True)
        return JsonResponse(source_team_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        source_team_data = JSONParser().parse(request)
        source_team_serializer = SourceTeamSerializer(data=source_team_data)
        if source_team_serializer.is_valid():
            source_team_serializer.save()
            return JsonResponse(source_team_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(source_team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        SourceTeam.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def source_team_detail(request, pk):
    try:
        source_team = SourceTeam.objects.get(pk=pk)
    except SourceTeam.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        source_team_serializer = SourceTeamSerializer(source_team)
        return JsonResponse(source_team_serializer.data)

    elif request.method == 'PUT':
        source_team_data = JSONParser().parse(request)
        source_team_serializer = SourceTeamSerializer(source_team, data=source_team_data)
        if source_team_serializer.is_valid():
            source_team_serializer.save()
            return JsonResponse(source_team_serializer.data)
        return JsonResponse(source_team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        source_team.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def source_team_list_id(request, id):
    source_team = SourceTeam.objects.filter(id=id)

    if request.method == 'GET':
        source_team_serializer = SourceTeamSerializer(source_team, many=True)
        return JsonResponse(source_team_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'