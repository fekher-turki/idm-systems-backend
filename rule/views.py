from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rule.models import Rule
from rule.serializers import RuleSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def rule_list(request):
    if request.method == 'GET':
        rule = Rule.objects.all()
        rule_serializer = RuleSerializer(rule, many=True)
        return JsonResponse(rule_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        rule_data = JSONParser().parse(request)
        rule_serializer = RuleSerializer(data=rule_data)
        if rule_serializer.is_valid():
            rule_serializer.save()
            return JsonResponse(rule_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(rule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Rule.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def rule_detail(request, pk):
    try:
        rule = Rule.objects.get(pk=pk)
    except Rule.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        rule_serializer = RuleSerializer(rule)
        return JsonResponse(rule_serializer.data)

    elif request.method == 'PUT':
        rule_data = JSONParser().parse(request)
        rule_serializer = RuleSerializer(rule, data=rule_data)
        if rule_serializer.is_valid():
            rule_serializer.save()
            return JsonResponse(rule_serializer.data)
        return JsonResponse(rule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rule.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def rule_list_id(request, id):
    rule = Rule.objects.filter(id=id)

    if request.method == 'GET':
        rule_serializer = RuleSerializer(rule, many=True)
        return JsonResponse(rule_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'