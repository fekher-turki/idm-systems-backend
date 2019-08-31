from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from currency.models import Currency
from currency.serializers import CurrencySerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def currency_list(request):
    if request.method == 'GET':
        currency = Currency.objects.all()
        currency_serializer = CurrencySerializer(currency, many=True)
        return JsonResponse(currency_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        currency_data = JSONParser().parse(request)
        currency_serializer = CurrencySerializer(data=currency_data)
        if currency_serializer.is_valid():
            currency_serializer.save()
            return JsonResponse(currency_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(currency_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Currency.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def currency_detail(request, pk):
    try:
        currency = Currency.objects.get(pk=pk)
    except Currency.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        currency_serializer = CurrencySerializer(currency)
        return JsonResponse(currency_serializer.data)

    elif request.method == 'PUT':
        currency_data = JSONParser().parse(request)
        currency_serializer = CurrencySerializer(currency, data=currency_data)
        if currency_serializer.is_valid():
            currency_serializer.save()
            return JsonResponse(currency_serializer.data)
        return JsonResponse(currency_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        currency.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def currency_list_id(request, id):
    currency = Currency.objects.filter(id=id)

    if request.method == 'GET':
        currency_serializer = CurrencySerializer(currency, many=True)
        return JsonResponse(currency_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'