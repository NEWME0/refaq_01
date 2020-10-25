from httpx import Client

from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi


class ProxySwaggerSchema:
    BASE_URL = 'http://127.0.0.1:8080/'
    OPENAPI_PATH = '/?format=openapi'

    @classmethod
    def get_openapi_json(cls):
        client = Client(base_url=cls.BASE_URL)
        response = client.get(cls.OPENAPI_PATH)
        return response.json()

    @classmethod
    def get_schema(cls):
        return None


class ProxyView(APIView):
    swagger_schema = ProxySwaggerSchema.get_schema()

    def dispatch(self, request, *args, **kwargs):
        """
        `.dispatch()` is pretty much the same as Django's regular dispatch,
        but with extra hooks for startup, finalize, and exception handling.
        """
        self.args = args
        self.kwargs = kwargs
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers  # deprecate?

        try:
            self.initial(request, *args, **kwargs)

            # Get the appropriate handler method
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, 'handler',
                                  self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            response = handler(request, *args, **kwargs)

        except Exception as exc:
            response = self.handle_exception(exc)

        self.response = self.finalize_response(request, response, *args, **kwargs)
        return self.response

    def handler(self, request, *args, **kwargs):
        request = self.request

        response = Response({
            'Hello': 'World'
        })

        return response
