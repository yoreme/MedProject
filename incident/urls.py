
from django.contrib import admin
from django.conf.urls import include, url
from . import views
from .views import Incident
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers


##test for swagger##
schema_view = get_schema_view(
    openapi.Info(
        title='Incident API',
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@test.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('api/v1/incidents', Incident)

urlpatterns = [
    url('', include(router.urls)),
    # url('get_report', incident.as_view({
    #     'get': 'retrieve',
    #     'patch': 'partial_update',
    # })),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
