from django.shortcuts import render
from django.http import HttpResponse
from .models import Incident
from .serializers import IncidentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class Incident(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    @action(detail=True, methods=['GET'])
    def incident_func(self, request, pk=None):
        response = {'message': 'its working fine'}
        return Response(response, status=status.HTTP_200_OK)


