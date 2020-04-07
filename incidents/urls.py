from django.urls import path,include
from . import views

urlpatterns=[
    path('list/',views.IncidentList.as_view()),
    path('create/',views.IncidentAPIView.as_view()),
    path('<int:id>',views.IncidentRetrieveUpdateDestroy.as_view(), name='update-delete-incident')
]