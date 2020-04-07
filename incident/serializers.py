from rest_framework import serializers
from .models import Incident


class IncidentPostSerializer(serializers.ModelSerializer):
     """Serializers registration requests and creates a new user."""
    place = serializers.CharField(max_length=128,
                                     write_only=True,
                                     required=True,)
    personalNumber = serializers.CharField(max_length=12,
                                     write_only=True,
                                     required=True,)
    description = serializers.CharField(max_length=255,max_length=255,style={'input_type': 'text'},write_only=True,
                                     required=True,) 
    action = serializers.CharField(max_length=255,style={'input_type': 'text'},write_only=True,
                                     required=True,)                 

    class Meta:
        model = Incident
        fields = ['place','personalNumber','description', 'action', ]

    def validate(self, attrs):
        place = attrs.get('place',None)
        personalNumber = attrs.get('personalNumber',None)
        description = attrs.get('description',None)
        action = attrs.get('action',None)

        #VALIDATION
        if place is None:
            raise serializers.ValidationError(
                'place is required.'
            )

        if personalNumber is None:
            raise serializers.ValidationError(
                'PersonalNumber is required.'
            )

        if description is None:
            raise serializers.ValidationError(
                'description is required.'
            )

        if action is None:
            raise serializers.ValidationError(
                'action is required.'
            )

        
        return attrs
    

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('place', 'time','action','description', 'personalNumber')