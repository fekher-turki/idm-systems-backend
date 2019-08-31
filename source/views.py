from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from source.models import Source
from source.serializers import SourceSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def source_list(request):
    if request.method == 'GET':
        source = Source.objects.all()
        source_serializer = SourceSerializer(source, many=True)
        return JsonResponse(source_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        source_data = JSONParser().parse(request)
        source_serializer = SourceSerializer(data=source_data)
        if source_serializer.is_valid():
            if source_data['date_start'] > source_data['date_end']:
                return JsonResponse(source_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            source_serializer.save()
            return JsonResponse(source_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(source_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Source.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def source_detail(request, pk):
    try:
        source = Source.objects.get(pk=pk)
    except Source.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        source_serializer = SourceSerializer(source)
        return JsonResponse(source_serializer.data)

    elif request.method == 'PUT':
        source_data = JSONParser().parse(request)
        source_serializer = SourceSerializer(source, data=source_data)
        if source_serializer.is_valid():
            source_serializer.save()
            return JsonResponse(source_serializer.data)
        return JsonResponse(source_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        source.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def source_list_id(request, id):
    source = Source.objects.filter(id=id)

    if request.method == 'GET':
        source_serializer = SourceSerializer(source, many=True)
        return JsonResponse(source_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'