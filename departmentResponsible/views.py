from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from departmentResponsible.models import DepartmentResponsible
from departmentResponsible.serializers import DepartmentResponsibleSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def department_responsible_list(request):
    if request.method == 'GET':
        department_responsible = DepartmentResponsible.objects.all()
        department_responsible_serializer = DepartmentResponsibleSerializer(department_responsible, many=True)
        return JsonResponse(department_responsible_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        department_responsible_data = JSONParser().parse(request)
        department_responsible_serializer = DepartmentResponsibleSerializer(data=department_responsible_data)
        if department_responsible_serializer.is_valid():
            department_responsible_serializer.save()
            return JsonResponse(department_responsible_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(department_responsible_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        DepartmentResponsible.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def department_responsible_detail(request, pk):
    try:
        department_responsible = DepartmentResponsible.objects.get(pk=pk)
    except DepartmentResponsible.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        department_responsible_serializer = DepartmentResponsibleSerializer(department_responsible)
        return JsonResponse(department_responsible_serializer.data)

    elif request.method == 'PUT':
        department_responsible_data = JSONParser().parse(request)
        department_responsible_serializer = DepartmentResponsibleSerializer(department_responsible, data=department_responsible_data)
        if department_responsible_serializer.is_valid():
            department_responsible_serializer.save()
            return JsonResponse(department_responsible_serializer.data)
        return JsonResponse(department_responsible_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        department_responsible.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def department_responsible_list_id(request, id):
    department_responsible = DepartmentResponsible.objects.filter(id=id)

    if request.method == 'GET':
        department_responsible_serializer = DepartmentResponsibleSerializer(department_responsible, many=True)
        return JsonResponse(department_responsible_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'