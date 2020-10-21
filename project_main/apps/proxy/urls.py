from django.urls import re_path
from .views import proxy_view


urlpatterns = [
    re_path(r'^(?P<url>.*)/$', proxy_view)
]
