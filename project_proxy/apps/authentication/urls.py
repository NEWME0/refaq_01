from django.urls import path
from .views import UserListCreateView


urlpatterns = [
    path('user/', UserListCreateView.as_view())
]
