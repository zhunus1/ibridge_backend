from django.shortcuts import render
from rest_framework import viewsets
from .models import Country
from rest_framework.renderers import JSONRenderer
from translations.models import CountryTranslation
from .serializers import (
    CountryDetailSerializer,
    CountryListSerializer
)

# Create your views here.

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    renderer_classes = (JSONRenderer,)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CountryListSerializer
        return CountryDetailSerializer