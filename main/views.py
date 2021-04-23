from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from . import serializers
from . import models



# Create your views here.
@csrf_exempt
@api_view(['POST'])
def home(request):
    profile, created = models.Profile.objects.get_or_create(employee_id=request.POST['employee_id'])
    
    profile.admin=request.POST['admin']
    profile.active=request.POST['active']
    profile.last_name=request.POST['last_name']
    profile.first_name=request.POST['first_name']
    profile.middle_name=request.POST['middle_name']
    profile.department=request.POST['department']
    profile.company=request.POST['company']
    profile.schedule=request.POST['schedule']

    profile.face_data1 = bytes(map(int,request.POST['face_data1'].split(' ')))
    profile.face_data2 = bytes(map(int,request.POST['face_data2'].split(' ')))
    profile.face_data3 = bytes(map(int,request.POST['face_data3'].split(' ')))

    profile.save()
    return HttpResponse(profile.id)


def sync(request):
    if request.method == 'GET':
        terminal, created = models.Terminal.objects.get_or_create(name=request.GET['terminal'])
        profiles = models.Profile.objects.all()
        if not created:
            profiles = profiles.filter(date_modified__gte=terminal.last_synced).exclude(owner=terminal)

        serializer = serializers.profile(profiles,many=True)
        terminal.save()

        return Response(serializer.data)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.profile