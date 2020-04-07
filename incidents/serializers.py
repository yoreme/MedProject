from rest_framework import serializers
from .models import Incident


class IncidentDetailSerializer(serializers.ModelSerializer):
     class Meta:
        model = Incident
        fields ='__all__'


class IncidentPostSerializer(serializers.ModelSerializer):
    """ Serializers registration requests and creates a new Incident."""
    place = serializers.CharField(required=True)
    personal_number = serializers.CharField(required=True)
    description = serializers.CharField(allow_blank=False, allow_null=False) 
    action = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Incident
        fields = ('place','personal_number','description', 'action')

    def validate(self, attrs):
        place = attrs.get('place',None)
        personal_number = attrs.get('personal_number',None)
        description = attrs.get('description',None)
        action = attrs.get('action',None)

        #VALIDATION
        if place is None:
            raise serializers.ValidationError(
                'place is required.'
            )

        if personal_number is None:
            raise serializers.ValidationError(
                'Personal Number is required.'
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
        fields = ('place','action','description', 'personal_number')




