from rest_framework.viewsets import ModelViewSet
from .serializers import FirstSerializer


class FirstViewSet(ModelViewSet):
    serializer_class = FirstSerializer

    def get_queryset(self):
        return []
