from django.shortcuts import render
from django.http import HttpResponse
from .models import Incident
from .serializers import IncidentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

class IncidentAPIView(APIView):
    serializer_class = IncidentPostSerializer

    def post(self, request):
        logger.info('Incident request data:{}'.format(request.data))
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            client_ip=get_client_ip(request)
            geo_location_response=
            data =serializer.validated_data
            Incident.object.create(place=data.get('place'),personalNumber=data.get('personalNumber'),description=data.get('description'),
            action=data.get('action'),ip_address=client_ip,latitude,longitude,
            country_name,country_code,city,region)
            response = {
                            'status': '00',
                            'message': "Incident was created successfully "
                        }
            logger.info('incident was created successfully')
            return Response(response, status=status.HTTP_200_OK)
        return Response({'message':'An error occurred while processing yur request','error':serializer.errors,}, status=status.HTTP_400_BAD_REQUEST)



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class Incident(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    @action(detail=True, methods=['GET'])
    def incident_func(self, request, pk=None):
        response = {'message': 'its working fine'}
        return Response(response, status=status.HTTP_200_OK)


