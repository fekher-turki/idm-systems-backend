from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from exchangeRate.models import ExchangeRate
from exchangeRate.serializers import ExchangeRateSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def exchangeRate_list(request):
    if request.method == 'GET':
        exchangeRate = ExchangeRate.objects.all()
        exchangeRate_serializer = ExchangeRateSerializer(exchangeRate, many=True)
        return JsonResponse(exchangeRate_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        exchangeRate_data = JSONParser().parse(request)
        exchangeRate_serializer = ExchangeRateSerializer(data=exchangeRate_data)
        if exchangeRate_serializer.is_valid():
            exchangeRate_serializer.save()
            return JsonResponse(exchangeRate_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(exchangeRate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ExchangeRate.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def exchangeRate_detail(request, pk):
    try:
        exchangeRate = ExchangeRate.objects.get(pk=pk)
    except ExchangeRate.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        exchangeRate_serializer = ExchangeRateSerializer(exchangeRate)
        return JsonResponse(exchangeRate_serializer.data)

    elif request.method == 'PUT':
        exchangeRate_data = JSONParser().parse(request)
        exchangeRate_serializer = ExchangeRateSerializer(exchangeRate, data=exchangeRate_data)
        if exchangeRate_serializer.is_valid():
            exchangeRate_serializer.save()
            return JsonResponse(exchangeRate_serializer.data)
        return JsonResponse(exchangeRate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        exchangeRate.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def exchangeRate_list_id(request, id):
    exchangeRate = ExchangeRate.objects.filter(id=id)

    if request.method == 'GET':
        exchangeRate_serializer = ExchangeRateSerializer(exchangeRate, many=True)
        return JsonResponse(exchangeRate_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'