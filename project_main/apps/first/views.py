from rest_framework.routers import SimpleRouter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import *
from .serializers import *


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def list(self, request, *args, **kwargs):
        return super(RecordViewSet, self).list(request, *args, **kwargs)

    @action(methods=['GET'], detail=False, url_path='list_01', url_name='list_01')
    def list_01(self, request, *args, **kwargs):
        RecordSerializer()
        return Response([])

    @action(methods=['GET'], detail=False, url_path='list_02', url_name='list_02')
    def list_02(self, request, *args, **kwargs):
        return Response([])

    @action(methods=['GET'], detail=False, url_path='list_03', url_name='list_03')
    def list_03(self, request, *args, **kwargs):
        return Response([])

    @action(methods=['GET'], detail=False, url_path='list_04', url_name='list_04')
    def list_04(self, request, *args, **kwargs):
        return Response([])


router = SimpleRouter()
