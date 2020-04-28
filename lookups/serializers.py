from django.utils.timezone import now
from datetime import datetime, date
from rest_framework import serializers
from .models import First_Category,Second_Category,Third_Category
from utils.common import is_date,valid_date
from django.db.models import Q
#m = models.SomeModel.objects.get(Q(id=model_id) | Q(name=model_name))

class FirstCategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = First_Category
        fields = ('id', 'name')
        

class FirstCategoryPostSerializer(serializers.ModelSerializer):
    """ Serializers registration requests for First Category."""
    name = serializers.CharField(required=True)

    class Meta:
        model = First_Category
        fields = ('id','name')
        read_only_Fields = ('id',)


class SecondCategoryDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    firstcategory_name = serializers.ReadOnlyField(source='firstcategory.name', read_only=True)


    class Meta:
        model = Second_Category
        fields = ('id', 'name','firstcategory','firstcategory_name','created_at')



class SecondCategoryPostSerializer(serializers.ModelSerializer):
    """ Serializers registration requests for First Category."""
    name = serializers.CharField(required=True)
    # firstcategory = serializers.HyperlinkedRelatedField(
    #     queryset=First_Category.objects.all(),
    #     lookup_field='name',
    #     view_name='firstcategory-list'
    # )

    class Meta:
        model = Second_Category
        fields = ('id','name','firstcategory')
        read_only_Fields = ('id',)




class ThirdCategoryDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    firstcategory_name = serializers.ReadOnlyField(source='firstcategory.name', read_only=True)
    secondcategory_name = serializers.ReadOnlyField(source='secondcategory.name', read_only=True)


    class Meta:
        model = Third_Category
        fields = ('id', 'name','firstcategory','firstcategory_name','secondcategory','secondcategory_name','created_at')



class ThirdCategoryPostSerializer(serializers.ModelSerializer):
    """ Serializers registration requests for First Category."""
    name = serializers.CharField(required=True)


    class Meta:
        model = Third_Category
        fields = ('id','name','firstcategory','secondcategory')
        read_only_Fields = ('id',)


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(use_url=False)