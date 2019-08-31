from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from sourceType.models import SourceType
from sourceType.serializers import SourceTypeSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def source_type_list(request):
    if request.method == 'GET':
        source_type = SourceType.objects.all()
        source_type_serializer = SourceTypeSerializer(source_type, many=True)
        return JsonResponse(source_type_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        source_type_data = JSONParser().parse(request)
        source_type_serializer = SourceTypeSerializer(data=source_type_data)
        if source_type_serializer.is_valid():
            source_type_serializer.save()
            return JsonResponse(source_type_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(source_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        SourceType.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def source_type_detail(request, pk):
    try:
        source_type = SourceType.objects.get(pk=pk)
    except SourceType.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        source_type_serializer = SourceTypeSerializer(source_type)
        return JsonResponse(source_type_serializer.data)

    elif request.method == 'PUT':
        source_type_data = JSONParser().parse(request)
        source_type_serializer = SourceTypeSerializer(source_type, data=source_type_data)
        if source_type_serializer.is_valid():
            source_type_serializer.save()
            return JsonResponse(source_type_serializer.data)
        return JsonResponse(source_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        source_type.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def source_type_list_id(request, id):
    source_type = SourceType.objects.filter(id=id)

    if request.method == 'GET':
        source_type_serializer = SourceTypeSerializer(source_type, many=True)
        return JsonResponse(source_type_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'