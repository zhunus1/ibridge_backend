from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet

router = DefaultRouter()
router.register(r'', PartnerViewSet, basename='')

urlpatterns = [] + router.urls
