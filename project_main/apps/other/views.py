from rest_framework.viewsets import ModelViewSet
from .serializers import OtherSerializer


class OtherViewSet(ModelViewSet):
    serializer_class = OtherSerializer

    def get_queryset(self):
        return []
