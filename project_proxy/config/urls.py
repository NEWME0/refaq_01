from django.urls import path, include
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('apps.authentication.urls'))
]


if settings.DEBUG:
    # Enable swagger
    from drf_yasg.views import get_schema_view
    from drf_yasg.openapi import Info
    from rest_framework.permissions import AllowAny

    info = Info(title='Proxy project', default_version='v1', description='...')
    schema = get_schema_view(info=info, permission_classes=(AllowAny,))
    swagger_view = schema.with_ui('swagger')

    urlpatterns += [
        path('', swagger_view),
    ]
