"""MedProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

schema_view = get_schema_view(
   openapi.Info(
      title="Med Proj API",
      default_version='v1',
      description="Med Proj description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="Med Proj License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('openapi/', TemplateView.as_view(template_name="swagger-ui/dist/index.html")),
    path('auth/',include('appAuths.urls')),
    path('docs/', schema_view,name='schema_view'),
    path('incidents/',include('incidents.urls')),
    path('descriptions/',include('descriptions.urls')),
    path('lookups/',include('lookups.urls'))
] 


if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)