from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from country.models import Country
from country.serializers import CountrySerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def country_list(request):
    if request.method == 'GET':
        country = Country.objects.all()
        country_serializer = CountrySerializer(country, many=True)
        return JsonResponse(country_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        country_data = JSONParser().parse(request)
        country_serializer = CountrySerializer(data=country_data)
        if country_serializer.is_valid():
            country_serializer.save()
            return JsonResponse(country_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Country.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def country_detail(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        country_serializer = CountrySerializer(country)
        return JsonResponse(country_serializer.data)

    elif request.method == 'PUT':
        country_data = JSONParser().parse(request)
        country_serializer = CountrySerializer(country, data=country_data)
        if country_serializer.is_valid():
            country_serializer.save()
            return JsonResponse(country_serializer.data)
        return JsonResponse(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def country_list_id(request, id):
    country = Country.objects.filter(id=id)

    if request.method == 'GET':
        country_serializer = CountrySerializer(country, many=True)
        return JsonResponse(country_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'