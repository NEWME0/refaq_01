from rest_framework.routers import DefaultRouter
from .views import OtherViewSet


router = DefaultRouter()
router.register('other', OtherViewSet, 'other')


urlpatterns = router.get_urls()
