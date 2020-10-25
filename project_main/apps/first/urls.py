from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register('records', RecordViewSet, 'records')
router.register('players', PlayerViewSet, 'players')

urlpatterns = router.get_urls()
