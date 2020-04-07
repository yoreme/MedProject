from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import serializers,viewsets,status,generics,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
import utils.geolocationservice as geolocation

from .models import Incident
from .serializers import IncidentSerializer,IncidentPostSerializer,IncidentDetailSerializer

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
logger.warn("Hello")
logger.error("Still here...")
logger.warn("Goodbye")

# Create your views here.


class IncidentAPIView(APIView):
    """ APIView for creating Incident as a POST Request """
    permission_classes = [AllowAny]
    serializer_class = IncidentPostSerializer

    def post(self, request):
        logger.info('Incident request data:{}'.format(request.data))
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            client_ip=get_client_ip(request)
            geo_location_response=geolocation.geolocationClient.get_location(client_ip)
            print(geo_location_response)
            logger.info('geo_location_response response:{}'.format(geo_location_response))
            data =serializer.validated_data
            if geo_location_response is not None:
                Incident.objects.create(place=data.get('place'),personal_number=data.get('personal_number'),
                description=data.get('description'),action=data.get('action'),
                ip_address=client_ip,latitude=geo_location_response['latitude'],
                longitude=geo_location_response['longitude'], country_name=geo_location_response['country_name'],
                country_code=geo_location_response['country_code'], city=geo_location_response['city'],
                region=geo_location_response['region'])
                response = {
                                'status': '00',
                                'message': "Incident was created successfully "
                            }
                logger.info('incident was created successfully')
                return Response(response, status=status.HTTP_200_OK)
        return Response({'message':'An error occurred while processing yur request','error':serializer.errors,}, status=status.HTTP_400_BAD_REQUEST)




class IncidentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """ APIView for updating,editing and deleting Incident it accept muliple HTTP Request get,post,delete etc """
    permission_classes = [AllowAny]
    serializer_class =IncidentDetailSerializer
    lookup_field = 'id'
    queryset = Incident.objects.all()

    def get_queryset(self):
        return get_object_or_404(Incident,id=self.kwargs.get(self.lookup_field))

    def get_object(self):
        return self.get_queryset()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, data=request.data,partial=partial)
        if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message':'An error occurred while processing yur request','error':serializer.errors,}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset()
        self.perform_destroy(instance)
        return Response({"message": "Incident has been successfully deleted"},status=status.HTTP_204_NO_CONTENT)



class IncidentList(generics.ListAPIView):
    """ APIView that returns list of  Incident a GET Request """
    permission_classes = [AllowAny]
    serializer_class=IncidentDetailSerializer
    queryset = Incident.objects.all()
    ordering_fields = ('created_at', 'personal_number')
    ordering=('created_at',)
    search_fields = ('created_at', 'personal_number')



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    @action(detail=True, methods=['GET'])
    def incident_func(self, request, pk=None):
        response = {'message': 'its working fine'}
        return Response(response, status=status.HTTP_200_OK)


