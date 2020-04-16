from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import serializers,viewsets,status,generics,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework_swagger import renderers

from .serializers import DescriptionPostSerializer

from scipy.stats import wasserstein_distance

# import the logging library
import logging
from drf_yasg.utils import swagger_auto_schema

from .Embeddings import Embeddings

# Get an instance of a logger
logger = logging.getLogger(__name__)
logger.warn("Initializing descriptions view")

embeddings = Embeddings()
embeddings.load_embeddings("c:\dev\swectors-300dim.txt")

# Create your views here.

class EmbeddingsAPIView(APIView):
    """ APIView for comparing two descriptions """
    permission_classes = [AllowAny]
    serializer_class = DescriptionPostSerializer

    @swagger_auto_schema(request_body=DescriptionPostSerializer)

    def post(self, request):
        logger.info('Description comparision request data:{}'.format(request.data))
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            data =serializer.validated_data
            fd = embeddings.get_w2v_sum(data['first_description'])
            sd = embeddings.get_w2v_sum(data['second_description'])
            res = wasserstein_distance(fd, sd)
            logger.warn(res)

            response = {
                            'status': '00',
                            'message': res
                        }
            logger.info('Comparision performed successfully')
            return Response(response, status=status.HTTP_200_OK)
        return Response({'message':'An error occurred while processing yur request','error':serializer.errors,}, status=status.HTTP_400_BAD_REQUEST)
