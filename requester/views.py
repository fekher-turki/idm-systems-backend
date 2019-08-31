from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from requester.models import Requester
from requester.serializers import RequesterSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def requester_list(request):
    if request.method == 'GET':
        requester = Requester.objects.all()
        requester_serializer = RequesterSerializer(requester, many=True)
        return JsonResponse(requester_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        requester_data = JSONParser().parse(request)
        requester_serializer = RequesterSerializer(data=requester_data)
        if requester_serializer.is_valid():
            requester_serializer.save()
            return JsonResponse(requester_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(requester_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Requester.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def requester_detail(request, pk):
    try:
        requester = Requester.objects.get(pk=pk)
    except Requester.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        requester_serializer = RequesterSerializer(requester)
        return JsonResponse(requester_serializer.data)

    elif request.method == 'PUT':
        requester_data = JSONParser().parse(request)
        requester_serializer = RequesterSerializer(requester, data=requester_data)
        if requester_serializer.is_valid():
            requester_serializer.save()
            return JsonResponse(requester_serializer.data)
        return JsonResponse(requester_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        requester.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def requester_list_id(request, id):
    requester = Requester.objects.filter(id=id)

    if request.method == 'GET':
        requester_serializer = RequesterSerializer(requester, many=True)
        return JsonResponse(requester_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'