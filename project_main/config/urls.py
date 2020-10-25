from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', include('apps.first.urls')),
    path('other/', include('apps.other.urls')),
    path('proxy/', include('apps.proxy.urls')),
]


if settings.DEBUG:
    # Enable swagger
    from drf_yasg.views import get_schema_view
    from drf_yasg.openapi import Info
    from rest_framework.permissions import AllowAny

    info = Info(title='Main project', default_version='v1', description='...')
    schema_view = get_schema_view(info=info, permission_classes=(AllowAny,))
    swagger_view = schema_view.with_ui('swagger')

    urlpatterns += [
        path('', swagger_view),
    ]
