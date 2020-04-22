from django.utils.timezone import now
from datetime import datetime, date
from rest_framework import serializers
from .models import Incident
from utils.common import is_date,valid_date


class IncidentDetailSerializer(serializers.ModelSerializer):
    days_since_incident = serializers.SerializerMethodField()

    class Meta:
        model = Incident
        fields ='__all__'

    def get_days_since_incident(self, obj):
        return (datetime.now().date() -  datetime.strptime(obj.incident_date, '%d-%m-%Y').date()).days


class IncidentPostSerializer(serializers.ModelSerializer):
    """ Serializers registration requests and creates a new Incident."""
    place = serializers.CharField(required=True)
    personal_number = serializers.CharField(required=True,max_length=12)
    description = serializers.CharField(max_length=100000,allow_blank=False, allow_null=False) 
    action = serializers.CharField(max_length=100000,allow_blank=True, allow_null=True)
    patient_firstname =  serializers.CharField(required=True)
    patient_lastname = serializers.CharField(required=True)
    suggestion =serializers.CharField(max_length=100000,allow_blank=False, allow_null=False) 
    patient_sex = serializers.ChoiceField(choices=Incident.SEXS,default=Incident.MALE)
    incident_type = serializers.ChoiceField(choices=Incident.INCIDENT_TYPES,default=Incident.RISK)
    incident_date= serializers.CharField(required=True)

    class Meta:
        model = Incident
        fields = ('place','personal_number','patient_firstname','patient_lastname','suggestion','patient_sex','description', 'action','incident_date','incident_type')

    def validate(self, attrs):
        place = attrs.get('place',None)
        personal_number = attrs.get('personal_number',None)
        description = attrs.get('description',None)
        action = attrs.get('action',None)
        incident_date=attrs.get('incident_date',None)

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

        if incident_date is not None:
            if is_date(incident_date) and valid_date(incident_date):
                if '-' in incident_date:
                    print('date has -')
                    convert_date=datetime.strptime(incident_date, '%d-%m-%Y')
                    print('The date is {}.'.format(convert_date))
                    incident_date =convert_date 
                elif '/' in  incident_date:
                    print('date has /')
                    convert__date=datetime.strptime(incident_date, '%d/%m/%Y')
                    print('The date is {}.'.format(convert__date))
                else:
                    print('date has no check')
                    incident_date=datetime.now()
            else:
                raise serializers.ValidationError(
                'incident date is required,Required Format DD-MM-YYYY.'
                )
        else:
            raise serializers.ValidationError(
                'incident date is required,Required Format DD-MM-YYYY.'
            )

        return attrs
    

        

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('place','action','description', 'personal_number')




