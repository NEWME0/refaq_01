from rest_framework.routers import DefaultRouter
from .views import FirstViewSet


router = DefaultRouter()
router.register('first', FirstViewSet, 'first')


urlpatterns = router.get_urls()
