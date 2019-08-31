from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from clientType.models import ClientType
from clientType.serializers import ClientTypeSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def client_type_list(request):
    if request.method == 'GET':
        client_type = ClientType.objects.all()
        client_type_serializer = ClientTypeSerializer(client_type, many=True)
        return JsonResponse(client_type_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        client_type_data = JSONParser().parse(request)
        client_type_serializer = ClientTypeSerializer(data=client_type_data)
        if client_type_serializer.is_valid():
            client_type_serializer.save()
            return JsonResponse(client_type_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(client_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ClientType.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def client_type_detail(request, pk):
    try:
        client_type = ClientType.objects.get(pk=pk)
    except ClientType.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        client_type_serializer = ClientTypeSerializer(client_type)
        return JsonResponse(client_type_serializer.data)

    elif request.method == 'PUT':
        client_type_data = JSONParser().parse(request)
        client_type_serializer = ClientTypeSerializer(client_type, data=client_type_data)
        if client_type_serializer.is_valid():
            client_type_serializer.save()
            return JsonResponse(client_type_serializer.data)
        return JsonResponse(client_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client_type.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def client_type_list_id(request, id):
    client_type = ClientType.objects.filter(id=id)

    if request.method == 'GET':
        client_type_serializer = ClientTypeSerializer(client_type, many=True)
        return JsonResponse(client_type_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'