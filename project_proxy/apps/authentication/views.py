from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer


users = [
    {
        'username': 'admin',
        'password': 'admin',
    },
    {
        'username': 'vasea',
        'password': 'vasea777',
    },
    {
        'username': 'refaq',
        'password': '<secret>',
    },
]


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return users

    def perform_create(self, serializer):
        queryset = self.get_queryset()
        queryset.append(serializer.data)
