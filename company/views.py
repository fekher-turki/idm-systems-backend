from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from company.models import Company
from company.serializers import CompanySerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        company = Company.objects.all()
        company_serializer = CompanySerializer(company, many=True)
        return JsonResponse(company_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        company_data = JSONParser().parse(request)
        company_serializer = CompanySerializer(data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse(company_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Company.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def company_detail(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        company_serializer = CompanySerializer(company)
        return JsonResponse(company_serializer.data)

    elif request.method == 'PUT':
        company_data = JSONParser().parse(request)
        company_serializer = CompanySerializer(company, data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse(company_serializer.data)
        return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def countCompany(request):
    if request.method == 'GET':
        company = Company.objects.count()
        count = [company]
        return JsonResponse(count, safe=False)
        # In order to serialize objects, we must set 'safe=False'


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def company_list_id(request, id):
    company = Company.objects.filter(id=id)

    if request.method == 'GET':
        company_serializer = CompanySerializer(company, many=True)
        return JsonResponse(company_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'