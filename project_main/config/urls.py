from django.urls import path, include
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', include('apps.first.urls')),
    path('other/', include('apps.other.urls')),
    path('proxy/', include('apps.proxy.urls')),
]


if settings.DEBUG:
    # Enable swagger
    from drf_yasg.views import get_schema_view
    from drf_yasg.openapi import Info, Swagger, Paths, Schema
    from drf_yasg.generators import OpenAPISchemaGenerator
    from rest_framework.permissions import AllowAny

    def get_openapi():
        import httpx
        response = httpx.get('http://127.0.0.1:8020/swagger/?format=openapi')
        return response.json()

    class ProxyOpenAPISchemaGenerator(OpenAPISchemaGenerator):
        def get_schema(self, request=None, public=False):
            swagger = super(ProxyOpenAPISchemaGenerator, self).get_schema(request, public)

            proxy_openapi = get_openapi()
            proxy_paths = {f'/proxy{key}': value for key, value in proxy_openapi['paths'].items()}
            proxy_paths = Paths(proxy_paths)
            proxy_definitions = {key: Schema(**value) for key, value in proxy_openapi['definitions'].items()}

            swagger.paths.update(proxy_paths)
            swagger.definitions.update(proxy_definitions)

            return swagger


    info = Info(title='Main project', default_version='v1', description='...')
    schema = get_schema_view(info=info, permission_classes=(AllowAny,), generator_class=ProxyOpenAPISchemaGenerator)

    print(schema)

    swagger_view = schema.with_ui('swagger')

    urlpatterns += [
        path('swagger/', swagger_view),
    ]
