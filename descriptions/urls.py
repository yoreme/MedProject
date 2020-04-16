from django.urls import path,include
from . import views

urlpatterns=[
    path('compare/',views.EmbeddingsAPIView.as_view())
]