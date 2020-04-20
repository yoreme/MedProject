from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema,TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING, TYPE_ARRAY



class ResponseSerializer(serializers.ModelSerializer):
    """ Compares likeness of two given incident descriptions."""
    message = serializers.CharField()
    status = serializers.CharField()
    data = serializers.CharField()
    error = serializers.DictField()




class ResponseField(serializers.JSONField):
    class Meta:
        swagger_schema_fields = {
            "type": TYPE_OBJECT,
            #"title": "Email",
            "properties": {
                "message":Schema(
                    title="message",
                    type=TYPE_STRING,
                ),
                "status": Schema(
                    title="status",
                    type=TYPE_INTEGER,
                ),
                "data": Schema(
                    title="data",
                    type=TYPE_OBJECT,
                ),
                "error": Schema(
                    title="status",
                    type=TYPE_STRING,
                )
            },
           # "required": ["subject", "body"],
        }