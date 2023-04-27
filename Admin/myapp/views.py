from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model,logout
# Create your views here.
class Med_Event(viewsets.ModelViewSet):
    queryset = MedicalCamp_event.objects.filter(Date__gt=timezone.now())
    serializer_class = McampSerializer

class Blood_Event(viewsets.ModelViewSet):
    queryset = Bloodcamp_event.objects.filter(date__gt=timezone.now())
    serializer_class = Bcampserializer

class Edu_Event(viewsets.ModelViewSet):
    queryset = Educational_event.objects.filter(date__gt=timezone.now())
    serializer_class = Ecampserializer

class CB_Event(viewsets.ModelViewSet):
    queryset = CBEmodel.objects.filter(date__gt=timezone.now())
    serializer_class = CBEserializer

class Animal_Event(viewsets.ModelViewSet):
    queryset = AnimalCampModel.objects.filter(date__gt=timezone.now())
    serializer_class = ACampserializer

class ForScribes_Event(viewsets.ModelViewSet):
    queryset = ForScribersModel.objects.filter(date__gt=timezone.now())
    serializer_class = SCampserializer

class App_Event(viewsets.ModelViewSet):
    queryset = ApplicantsModel.objects.all()
    serializer_class = APCampserializer

# event history api's
class MedcampHis(viewsets.ModelViewSet):
    queryset = MedicalCamp_event.objects.all().order_by('-Date')
    serializer_class = McampSerializer

class BcampHis(viewsets.ModelViewSet):
    queryset = Bloodcamp_event.objects.all().order_by('-date')
    serializer_class = Bcampserializer

class EducampHis(viewsets.ModelViewSet):
    queryset = Educational_event.objects.all().order_by('-date')
    serializer_class = Ecampserializer

class CBEcampHis(viewsets.ModelViewSet):
    queryset = CBEmodel.objects.all().order_by('-date')
    serializer_class = CBEserializer

class AnmcampHis(viewsets.ModelViewSet):
    queryset = AnimalCampModel.objects.all().order_by('-date')
    serializer_class = ACampserializer

class SCcampHis(viewsets.ModelViewSet):
    queryset = ForScribersModel.objects.all().order_by('-date')
    serializer_class = SCampserializer

class APcampHis(viewsets.ModelViewSet):
    queryset = ApplicantsModel.objects.all()
    serializer_class = APCampserializer


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "You have been logged out."})