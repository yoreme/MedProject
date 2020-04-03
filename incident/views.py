from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ReportIncident

# Create your views here.
class CreateIncident(View):
    
    def get(self, request):
        return HttpResponse('testing functions in class')

class GetIncident(View):
    
    incedents = ReportIncident.objects.all()
    currentIncident = ''

    currentIncident += f"You currently have {len(incedents)} reported incident <br>"

    for incident in incedents:
        currentIncident += f"{incident.place} {incident.time} {incident.action} "

    def get(self, request):
        return HttpResponse(self.currentIncident)

def testing(request):
    return HttpResponse('testing message from view')