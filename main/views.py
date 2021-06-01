from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from . import serializers
from . import models

import json


# methods
def createOrUpdateUser(userDetail, terminal, site):
    profile, created = models.Profile.objects.get_or_create(
        employee_id=userDetail['employee_id'])

    profile.site = site
    profile.owner = terminal
    profile.admin = userDetail['admin']
    profile.active = userDetail['active']
    profile.last_name = userDetail['last_name']
    profile.first_name = userDetail['first_name']
    profile.middle_name = userDetail['middle_name']
    profile.department = userDetail['department']
    profile.company = userDetail['company']
    profile.schedule = userDetail['schedule']

    profile.face_data1 = bytes(
        map(int, userDetail['face_data1_string'].split(' ')))
    profile.face_data2 = bytes(
        map(int, userDetail['face_data2_string'].split(' ')))
    profile.face_data3 = bytes(
        map(int, userDetail['face_data3_string'].split(' ')))

    profile.save()
    return profile.id


# Create your views here.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user(request):
    id = createOrUpdateUser(request.POST)
    return HttpResponse(id)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sync(request):
    if request.auth:
        if request.method == 'GET':
            last_synced = request.GET['last_synced']

            if last_synced == '0001-01-01T00:00:00':
                profiles = models.Profile.objects.all()
            else:
                profiles = models.Profile.objects.filter(
                    date_modified__gte=last_synced)
           
            profiles = profiles.filter(site=request.GET['site']).exclude(owner=request.GET['terminal'])

            serializer = serializers.Profile(profiles, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            data = json.loads(request.body)
            for user in data['users']:
                createOrUpdateUser(user, data['terminal'],data['site'])
            return Response("sync success")
    return HttpResponse(request.auth)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.Profile