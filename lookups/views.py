from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import serializers,viewsets,status,generics,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework_swagger import renderers

from .serializers import (FirstCategoryDetailSerializer,FirstCategoryPostSerializer,SecondCategoryDetailSerializer,
SecondCategoryPostSerializer,ThirdCategoryDetailSerializer,ThirdCategoryPostSerializer,FileUploadSerializer)

from .models import First_Category,Second_Category,Third_Category
# import the logging library
import logging
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING, TYPE_ARRAY

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.parsers import  FileUploadParser,MultiPartParser, FormParser

import os
from datetime import datetime
import uuid

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.

class FirstCategoryAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = FirstCategoryPostSerializer

    @swagger_auto_schema(operation_description="post description override",request_body=FirstCategoryPostSerializer,
        responses={status.HTTP_200_OK: Schema(type=TYPE_OBJECT)})

    def post(self, request):
        logger.info('First Category request data:{}'.format(request.data))
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if First_Category.objects.filter(name=serializer.validated_data['name']).exists():
                return Response({'message':'name already exist!','error':serializer.errors,}, status=status.HTTP_400_BAD_REQUEST)  
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message':'An error occurred while processing yur request','error':serializer.errors,}, status=status.HTTP_400_BAD_REQUEST)


        
class FirstCategoryList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FirstCategoryDetailSerializer
    queryset = First_Category.objects.all()
    ordering_fields = ('created_at')
    ordering=('created_at',)



class SecondCategoryAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SecondCategoryPostSerializer

    @swagger_auto_schema(operation_description="post description override",request_body=SecondCategoryPostSerializer,
        responses={status.HTTP_200_OK: Schema(type=TYPE_OBJECT)})

    def post(self, request):
        logger.info('First Category request data:{}'.format(request.data))
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if Second_Category.objects.filter(name=serializer.validated_data['name'],firstcategory=serializer.validated_data['firstcategory']).exists():
                return Response({'message':'Name and Category already exist!','error':serializer.errors,}, status=status.HTTP_400_BAD_REQUEST)  
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message':'An error occurred while processing yur request','error':serializer.errors,}, status=status.HTTP_400_BAD_REQUEST)


        
class SecondCategoryList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SecondCategoryDetailSerializer
    ordering_fields = ('created_at')
    ordering=('created_at',)

    def get_queryset(self):
        """
        This view should return a list of all the second Category list.
        """ 
        queryset = Second_Category.objects.all()
        firstcategory = self.request.query_params.get('firstcategory', None)
        logger.info('firstcategory query_params:{}'.format(firstcategory))
        if firstcategory is not None:
            queryset = queryset.filter(firstcategory_id=firstcategory)

        return queryset



class FileUploadView(APIView):
    """
        A view that can accept POST requests with JSON content.
    """
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    serializer=FileUploadSerializer
    valid_extensions = ['.txt']
    lookup_field = 'firstcategoryid'  

    def put(self,request,**kwargs):
        success_count=0
        duplicate_count=0
        total_item_count=0
        firstcategoryid=self.kwargs.get(self.lookup_field)
        now = datetime.now() # current date and time
        serializer = self.serializer(data=request.FILES)
        if serializer.is_valid():
            file_data = serializer.validated_data['file']
            file_extension = os.path.splitext(file_data.name)[1]
            logger.info('file extension :{}'.format(file_extension))
            new_path = settings.MEDIA_ROOT + f'/upload/{now.strftime("%Y")}/{now.strftime("%m")}/{now.strftime("%d")}' 
            file_name=str(uuid.uuid1())+file_data.name
            logger.info('file name :{}'.format(file_name))
            fs = FileSystemStorage(location=new_path)  
            path=fs.save(file_name,file_data)
            logger.info('filestorage file path :{}'.format(path))
            firstcategory=First_Category.objects.get(id=firstcategoryid)
            if not file_extension in self.valid_extensions:
                raise ValidationError("file not in correct format, must be txt,current format '{0}'".format(file_extension))
            if file_extension =='.txt': 
                with open(os.path.join(new_path,file_name),'r') as f:
                    content=f.readlines()
                    for line in content[0:]:
                        total_item_count +=1
                        line=line.strip()
                        if line is not None:
                            if not Second_Category.objects.filter(name=line,firstcategory=firstcategoryid).exists():
                                secondcategory_data = {
                                "name": line,
                                "firstcategory":firstcategory}
                                Second_Category.objects.create(**secondcategory_data)
                                success_count +=1
                            else:
                                duplicate_count +=1
                            
                if fs.exists(file_name):
                    logger.info('file exist,now going to delete')
                    fs.delete(file_name)

                return Response({'success': 'Imported successfully','total Item':f'{total_item_count}', 'duplicate':f'{duplicate_count}', 'sucessfully processed':f'{success_count}'},status=200)
        else:
            return Response(serializer.errors, status=400)



class ThirdCategoryAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ThirdCategoryPostSerializer

    @swagger_auto_schema(operation_description="post description override",request_body=ThirdCategoryPostSerializer,
        responses={status.HTTP_200_OK: Schema(type=TYPE_OBJECT)})

    def post(self, request):
        logger.info('First Category request data:{}'.format(request.data))
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if Third_Category.objects.filter(name=serializer.validated_data['name'],firstcategory=serializer.validated_data['firstcategory'],
            secondcategory=serializer.validated_data['secondcategory']).exists():
                return Response({'message':'Name and Categories already exist!','error':serializer.errors,}, status=status.HTTP_400_BAD_REQUEST)  
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message':'An error occurred while processing yur request','error':serializer.errors,}, status=status.HTTP_400_BAD_REQUEST)


        
class ThirdCategoryList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ThirdCategoryDetailSerializer
    queryset = Third_Category.objects.all()
    ordering_fields = ('created_at')
    ordering=('created_at',)
