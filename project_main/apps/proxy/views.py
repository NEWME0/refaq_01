import httpx

from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


def proxy_view(request, *args, **kwargs):
    return Response({
        'args': args,
        'kwargs': kwargs
    })
