from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    CountryViewSet,
)

router = DefaultRouter()
router.register(r'', CountryViewSet)

urlpatterns = [] + router.urls
