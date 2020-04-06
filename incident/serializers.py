from rest_framework import serializers
from .models import ReportIncident

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportIncident
        fields = ('place', 'time','action','description', 'personalNumber')